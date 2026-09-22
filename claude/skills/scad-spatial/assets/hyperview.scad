// hyperview.scad — a 4D object seen through a 3D camera four different ways.
// OpenSCAD 2021.01 compatible.  Render:  bash render.sh
//
//   MODE = "rotate"  perspective-project 4D->3D; $t spins the x-w plane
//          "shadow"  orthographic (drop w); the classic cube-inside-a-cube
//          "slice"   show only the 3D cross-section in a scrubbed z-slab
//          "project" Schlegel-style: push the +w cell toward the eye
//
// The point of the asset: ONE 4D thing, and every picture of it is a 3D
// shadow / slice.  Change MODE and $t and watch which structure survives.

MODE   = "rotate";      // rotate | shadow | slice | project
OBJ    = "tesseract";   // tesseract | 16cell
D4     = 3.0;           // 4D perspective eye distance (w-axis)
EDGE_R = 0.045;         // edge tube radius (fraction of unit)
NODE_R = 0.09;
SLAB   = 0.30;          // slice thickness, in projected-z units
GNOMON = true;

// ── canonical camera presets — pass one to render.sh / --camera $vpr ────────
// front [90,0,0]  top [0,0,0]  right [90,0,90]  iso [55,0,25]
$fn = 24;

// ── 4D vertices ────────────────────────────────────────────────────────────
function tesseract_v() = [ for (a=[-1,1], b=[-1,1], c=[-1,1], d=[-1,1]) [a,b,c,d] ];
function sixteen_v()   = [ for (i=[0:3], s=[-1,1]) [ for (k=[0:3]) (k==i? s: 0) ] ];

V4 = (OBJ=="16cell") ? sixteen_v() : tesseract_v();

// edges: connect vertices at Hamming/coord distance that makes the 1-skeleton
function edist(p,q) = sqrt( (p[0]-q[0])*(p[0]-q[0]) + (p[1]-q[1])*(p[1]-q[1])
                          + (p[2]-q[2])*(p[2]-q[2]) + (p[3]-q[3])*(p[3]-q[3]) );
EDGE_LEN = (OBJ=="16cell") ? sqrt(2) : 2;   // nearest-neighbour distance
EDGES = [ for (i=[0:len(V4)-1], j=[i+1:len(V4)-1])
            if (abs(edist(V4[i],V4[j]) - EDGE_LEN) < 1e-6) [i,j] ];

// ── 4D rotate (x-w plane) then project to 3D ───────────────────────────────
function rot_xw(p, a) =
    [ p[0]*cos(a) - p[3]*sin(a), p[1], p[2], p[0]*sin(a) + p[3]*cos(a) ];

function project(p) =
    (MODE=="shadow")
        ? [p[0], p[1], p[2]]                                   // drop w
  : (MODE=="project")
        ? let (k = D4 / (D4 - 1.6*p[3])) [p[0]*k, p[1]*k, p[2]*k]
        : let (k = D4 / (D4 - p[3]))     [p[0]*k, p[1]*k, p[2]*k]; // perspective

ANG = (MODE=="rotate" || MODE=="slice") ? 360*$t : 22;
P3  = [ for (p=V4) project(rot_xw(p, ANG)) ];

// ── draw ───────────────────────────────────────────────────────────────────
module edge(a, b) {
    hull() { translate(a) sphere(EDGE_R); translate(b) sphere(EDGE_R); }
}
module wireframe() {
    color([0.62,0.28,0.95]) {
        for (e = EDGES) edge(P3[e[0]], P3[e[1]]);
        for (p = P3) translate(p) sphere(NODE_R);
    }
}
module gnomon() {
    if (GNOMON) {
        L = 1.9;
        color("red")   { translate([0,0,0]) rotate([0,90,0])  cylinder(h=L, r=0.02); translate([L,0,0]) text3d("x"); }
        color("green") { rotate([-90,0,0]) cylinder(h=L, r=0.02);                     translate([0,L,0]) text3d("y"); }
        color("blue")  { cylinder(h=L, r=0.02);                                       translate([0,0,L]) text3d("z"); }
        color([1,1,1,0.15]) cube(2*[1,1,1], center=true);   // unit bounding box
    }
}
module text3d(s) { linear_extrude(0.01) text(s, size=0.28, halign="center"); }

scale(12) {
    if (MODE=="slice") {
        lvl = 2*($t*2 % 1) - 1;                 // scrub z-level with $t
        intersection() { wireframe(); translate([0,0,lvl]) cube([4,4,SLAB], center=true); }
        color([1,1,1,0.08]) translate([0,0,lvl]) cube([4,4,SLAB], center=true);
    } else {
        wireframe();
    }
    gnomon();
}

echo(str("MODE=", MODE, "  OBJ=", OBJ, "  edges=", len(EDGES), "  angle=", ANG));

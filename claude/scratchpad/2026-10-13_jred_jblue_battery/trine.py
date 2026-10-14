"""Documented trine (Ainulindale wiki 70): [J_blue,J_red]=J_green, [J_red,J_green]=J_blue, [J_green,J_blue]=J_red (su(2)). Which sedenion triples realise it, and where do they sit in the red/blue grading?"""
exec(open('jb.py').read().split('print("JB-1')[0])
E=np.eye(16); br=lambda x,y:m(x,y)-m(y,x)
found=[]
for r in (1,2,3):                      # red imaginary units
    for b in (4,5,6,7):                # blue units
        g=br(E[b],E[r])
        if nz(g)<1e-9: continue
        gi=int(np.argmax(np.abs(g))); sg=g[gi]/2           # [b,r]=2 b r = +-2 e_g
        # su(2) closure with factors: check the cyclic relations up to the common factor 2 and signs
        c1=br(E[r],E[gi]); c2=br(E[gi],E[b])
        ok = abs(abs(np.dot(c1,E[b]))-2)<1e-9 and abs(abs(np.dot(c2,E[r]))-2)<1e-9
        found.append((r,b,gi,round(sg,1),ok,'blue' if gi in BLUE else 'red'))
print("(red,blue,green index, sign, closes as quaternion line, grade of green):"); [print("  ",f) for f in found]
print("lines with red J_red, blue J_blue and J_green=[J_blue,J_red]:",sum(1 for f in found if f[4]),"; all green in blue half:",all(f[5]=='blue' for f in found))

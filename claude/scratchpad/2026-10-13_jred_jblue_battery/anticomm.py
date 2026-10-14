exec(open('jb.py').read().split('print("JB-1')[0])
w=[]
for _ in range(200):
    r=vec(RED[1:]); b=vec(BLUE); w.append(nz(m(r,b)+m(b,r)))
print("pure-imaginary J_red element r (no e0) and J_blue element b: max |rb+br| = %.1e  (exact anticommutation: r*b = -b*r = [r,b]/2)"%max(w))
r=vec(RED); b=vec(BLUE); print("with the e0 part of J_red included: |rb+br| = %.3f = 2|r0| |b| = %.3f"%(nz(m(r,b)+m(b,r)),2*abs(r[0])*nz(b)))

"""T6: how many different 97-symbol orders does the code base carry, and what is the permutation between them?"""
import importlib.util, math, sys
def load(name,path):
    s=importlib.util.spec_from_file_location(name,path); m=importlib.util.module_from_spec(s); s.loader.exec_module(m); return m
R='/home/rendier/Projects/ThePlace/'
ds=load('ds',R+'PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py'); kb=ds.HyperWebster._DEFAULT_CHARS
sys.path.insert(0,R)
uni=''.join(sorted([chr(i) for i in range(0x20,0x7f)]+['\t','\n'],key=ord))
vq=load('vq',R+'ValaQuenta/modules/hyperwebster/maths.py').US_KEYBOARD_CHARS
orders={'keyboard-row (Data-Storage/manifold/archimedes/gallery/layer3)':kb,'Unicode ord (Callimachus v09 PUBLIC, kcf)':uni,'ValaQuenta US_KEYBOARD_CHARS':vq}
for k,v in orders.items(): print(f"{len(v):3d} symbols, distinct {len(set(v))}, same alphabet as Unicode: {set(v)==set(uni)} : {k}")
def addr(s,order):   # bijective, shipping form
    N=len(order); a=0
    for c in s: a=a*N+order.index(c)+1
    return a-1
for w in ("hello","Ptolemy"):
    print(w,{k.split(' ')[0]:addr(w,v) for k,v in orders.items()})
def cycles(p):
    seen=set();out=[]
    for i in range(len(p)):
        if i in seen: continue
        n=0;j=i
        while j not in seen: seen.add(j);j=p[j];n+=1
        out.append(n)
    return sorted(out,reverse=True)
sig=[uni.index(c) for c in kb]      # keyboard index -> unicode index
cy=cycles(sig); print("keyboard->Unicode permutation cycle type:",cy[:10],"... fixed points:",cy.count(1),"order (lcm):",math.lcm(*cy))
print(f"97! = 2^{math.log2(math.factorial(97)):.1f};  257-bit? fits in 64 bytes: {math.factorial(97).bit_length()} bits")

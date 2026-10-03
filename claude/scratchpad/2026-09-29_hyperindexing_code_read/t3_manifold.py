"""T3: CharacterManifold bits vs naive vs information floor (multinomial), and what is left out of the bit count."""
import importlib.util, math
from collections import Counter
p='/home/rendier/Projects/ThePlace/PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster_manifold.py'
spec=importlib.util.spec_from_file_location('m',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
M=m.CharacterManifold()
txt=open('/home/rendier/Projects/ThePlace/Ainulindale/README.md',encoding='utf-8',errors='ignore').read()
txt=''.join(c for c in txt if c in M._char_idx)
for L in (140,1000,4000):
    t=txt[:L]; ma=M.decompose(t); ok=M.reconstruct(ma)==t
    c=Counter(t)
    multinom=math.lgamma(L+1)-sum(math.lgamma(k+1) for k in c.values()); multinom/=math.log(2)
    print(f"L={L}: round-trip {ok}; naive L*log2(97)={L*math.log2(97):.0f}; manifold sum(sub_bits)={ma.total_sub_bits()}; "
          f"info floor log2(multinomial)={multinom:.0f} (+ counts, + which chars); active dims {ma.n_active}")

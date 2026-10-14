import sys,time
sys.path.insert(0,'/home/rendier/Projects/ThePlace/VAPMIP')
t=time.time()
from rotary_rerun_boxkite_monad import RotaryBoxKiteMonad
m=RotaryBoxKiteMonad(); print("init %.1fs"%(time.time()-t))
for p in ["finger pointer","can you play the piano?","what is a tree","neutron generation in different reactor types"]:
    t=time.time(); e=m.process_input(p); dt=(time.time()-t)*1000
    print(f"{dt:7.0f} ms | {p!r} -> {getattr(e,'response',None) or e}")

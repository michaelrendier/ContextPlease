import sys, itertools, time
sys.argv=['x']
src=open('/home/rendier/Projects/ThePlace/VAPMIP/RingCircle/ring_circle_battery.py').read().split("gens = {")[0]
__file__='/home/rendier/Projects/ThePlace/VAPMIP/RingCircle/ring_circle_battery.py'
exec(src)
print('pair {1,10}',alg_dim([LK[1],LK[10]]),' {1,9}',alg_dim([LK[1],LK[9]]),' {1,2,10}',alg_dim([LK[1],LK[2],LK[10]]),' {1,8}',alg_dim([LK[1],LK[8]]))
for size in (5,6,7,8):
    t=time.time(); good=[s for s in itertools.combinations(range(1,16),size) if alg_dim([LK[k] for k in s])==256]
    tot=len(list(itertools.combinations(range(1,16),size)))
    print(size,'generate full 256:',len(good),'of',tot,good[:4],round(time.time()-t,1),'s',flush=True)
    if good: break

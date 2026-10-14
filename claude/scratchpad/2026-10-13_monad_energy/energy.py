"""Energy per monad reply from battery discharge (AC unplugged). Idle baseline -> load (ptolemy -r -n, long stdin) -> idle baseline."""
import time, subprocess, threading, statistics as st, os, sys
B='/sys/class/power_supply/BAT0/'
rd=lambda f:open(B+f).read().strip()
def sample(sec,out):
    t0=time.time()
    while time.time()-t0<sec:
        out.append((time.time(),int(rd('power_now'))/1e6,int(rd('energy_now'))/1e6)); time.sleep(0.5)
def phase_idle(sec):
    s=[]; sample(sec,s); return s
assert rd('status')=='Discharging', rd('status')
N=int(sys.argv[1]) if len(sys.argv)>1 else 5000
open('/tmp/claude-1000/replies_in.txt','w').write(("what is a tree\nexamine the reactor\ngo north\nask about primes\n"*(N//4))+"\n")
idle1=phase_idle(40)
s=[]; th=threading.Thread(target=sample,args=(70,s)); th.start()
t0=time.time(); p=subprocess.run(['/home/rendier/Projects/ThePlace/VAPMIP/PtolC/ptolemy','-r','-n'],stdin=open('/tmp/claude-1000/replies_in.txt'),stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL,cwd='/home/rendier/Projects/ThePlace/VAPMIP/PtolC'); t1=time.time()
th.join()
idle2=phase_idle(40)
load=[x for x in s if t0<=x[0]<=t1]; dur=t1-t0; lines=(N//4)*4
mi=st.mean([x[1] for x in idle1+idle2]); sdi=st.pstdev([x[1] for x in idle1+idle2]); ml=st.mean([x[1] for x in load])
print(f"AC offline; idle mean {mi:.3f} W (sd {sdi:.3f}, n={len(idle1+idle2)}); idle1 {st.mean([x[1] for x in idle1]):.3f} idle2 {st.mean([x[1] for x in idle2]):.3f}")
print(f"load: {lines} replies in {dur:.1f} s ({dur/lines*1000:.1f} ms/reply); mean {ml:.3f} W over {len(load)} samples; exit {p.returncode}")
d=ml-mi; E=d*dur
print(f"delta {d:.3f} W -> {E:.2f} J = {E/3.6:.2f} mWh for the run -> {E/lines*1000:.3f} mJ = {E/lines/3.6*1000:.4f} uWh per reply")
print(f"battery energy_now: start {idle1[0][2]:.3f} Wh, after load {s[-1][2]:.3f} Wh, end {idle2[-1][2]:.3f} Wh")

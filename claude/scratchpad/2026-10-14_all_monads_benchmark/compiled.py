"""The compiled voices on the SAME six prompts: ptolemy -r -n (Zork REPL, in-process monad), ptol -say (sentence creator via Python), ptol (plain word bag)."""
import subprocess, time, json, resource, os
PC='/home/rendier/Projects/ThePlace/VAPMIP/PtolC'
P=["finger pointer","what is a tree","neutron generation in different reactor types","good morning","can you play the piano?","the first reactor was built after neutrons were discovered"]
res={}
# REPL: replies of one 6-line session, then timing over 600 lines
p=subprocess.run([PC+'/ptolemy','-r','-n'],input="\n".join(P)+"\n\n",capture_output=True,text=True,cwd=PC,timeout=120)
lines=[l for l in p.stdout.splitlines() if l.strip() and not l.startswith('>>>') and not l.startswith(' ') and not l.startswith('[')]
res['ptolemy -r replies']=[l.strip() for l in p.stdout.replace('>>> ','\n').splitlines() if l.strip() and not l.startswith('[') and not l.startswith(' ')][:12]
open('/tmp/claude-1000/rin.txt','w').write("\n".join(P*100)+"\n\n")
t=time.time(); r0=resource.getrusage(resource.RUSAGE_CHILDREN)
p=subprocess.run([PC+'/ptolemy','-r','-n'],stdin=open('/tmp/claude-1000/rin.txt'),capture_output=True,text=True,cwd=PC,timeout=300)
dt=time.time()-t; r1=resource.getrusage(resource.RUSAGE_CHILDREN)
res['ptolemy -r timing']={'lines':600,'wall_s':round(dt,2),'ms_per_line':round(dt/600*1000,1),'cpu_s':round((r1.ru_utime+r1.ru_stime)-(r0.ru_utime+r0.ru_stime),2),'maxrss_mb':round(r1.ru_maxrss/1024,0)}
for mode,args in (('ptol -say',['-say']),('ptol plain',[])):
    out=[]
    for q in P:
        t=time.time(); p=subprocess.run([PC+'/ptol']+args+[q],capture_output=True,text=True,cwd=PC,timeout=120); out.append({'prompt':q,'ms':round((time.time()-t)*1000),'reply':[l for l in p.stdout.splitlines() if l.strip() and not l.startswith('  [') and not l.startswith('paper:')][-1:]})
    res[mode]=out
json.dump(res,open('results_compiled.json','w'),indent=1)
print(json.dumps(res,indent=1)[:3500])

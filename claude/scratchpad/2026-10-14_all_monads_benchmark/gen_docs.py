import json, statistics as st, os
H=os.path.dirname(os.path.abspath(__file__)); L=lambda f: json.load(open(os.path.join(H,f)))
con=L('results_console_loader.json'); ext=L('results_extra.json'); cmp_=L('results_compiled.json'); via=L('results_orbweaver_via.json')
BASE_W=9.255          # measured whole-laptop mean (battery run 2026-10-13), used where the per-voice run was too short to sample power
rows=[]
def add(group,r):
    c1=[c for c in r['calls'] if c['round']==1]; c2=[c for c in r['calls'] if c['round']==2]
    warm=st.mean(c['ms'] for c in c2); w=r.get('warm_mean_W'); wl='measured' if w else 'derived'; W=w or BASE_W
    rows.append(dict(group=group,name=r['name'],kind=r['adapter'],load=r['load_s'],rss=round(r['rss_loaded_mb']-r.get('rss_console_mb',r['rss_start_mb']),1),
      first=round(st.mean(c['ms'] for c in c1),1),warm=round(warm,2),cpu=round(r['warm_cpu_s']/6*1000,1),W=W,wl=wl,uwh=W*warm/3.6,errs=sum(1 for c in r['calls'] if c['error']),calls=c2))
for r in con:
    if not r.get('error'): add('A: console `/monad use` loads it',r)
for r in ext: add('B: own entry point (not seen by the console loader)',r)
fmt=lambda x:(f"{x:,.1f}" if x>=10 else f"{x:.2f}")
md=["| Voice (module.class.method or adapter) | load s | RSS +MB | 1st-round ms | warm ms | whole-laptop µWh per reply | vs 0.3 Wh |","|---|---|---|---|---|---|---|"]
for r in sorted(rows,key=lambda r:r['warm']):
    md.append(f"| {r['name']} ({r['kind']}) | {r['load']} | {r['rss']} | {fmt(r['first'])} | {fmt(r['warm'])} | {fmt(r['uwh'])} ({r['wl']} {r['W']} W) | {0.3e6/r['uwh']:,.0f}× lower |")
tbl="\n".join(md)
def clean(s): return (s or '').replace(' ',' ').replace(' ',' ').replace(' ',' ').replace(' ',' ').replace('\n',' ⏎ ')
tr=[]
for r in sorted(rows,key=lambda r:r['warm']):
    tr.append(f"\n**{r['name']}** ({r['kind']})\n```\n"+"\n".join(f"> {c['prompt']}\n{clean(c['reply'] or c['error'])[:210]}" for c in r['calls'])+"\n```")
comp=cmp_['ptolemy -r timing']
open(os.path.join(H,'tables.md'),'w').write(tbl+"\n")
open(os.path.join(H,'transcripts.md'),'w').write("\n".join(tr)+"\n")
print(tbl); print(); print(comp); print(len(rows),"voices")
json.dump(rows,open(os.path.join(H,'rows.json'),'w'),indent=1,default=str)

"""T5: PRIVATE charset (a permutation of the alphabet) == monoalphabetic substitution applied before the public address.
Then: an observer who knows only N (the base) recovers the substituted text from the integer and frequency-analyses it."""
import random, math, importlib.util
from collections import Counter
p='/home/rendier/Projects/ThePlace/PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster.py'
spec=importlib.util.spec_from_file_location('hw',p); hw=importlib.util.module_from_spec(spec); spec.loader.exec_module(hw)
pub=hw.HyperWebster(); chars=list(pub.characters)
rnd=random.Random(1); perm=chars[:]; rnd.shuffle(perm)
priv=hw.HyperWebster(''.join(perm))
txt=open('/home/rendier/Projects/ThePlace/Ainulindale/README.md',encoding='utf-8',errors='ignore').read()
txt=''.join(c for c in txt if c in pub._char_index)[:3000]
addr=priv.point_to_text(txt)
# identity: private address == public address of the substituted text
sub={c:perm_c for c,perm_c in zip(perm,chars)}     # private digit d -> public char chars[d]
print("addr_priv(s) == addr_pub(pi(s)):", addr==pub.point_to_text(''.join(chars[perm.index(c)] for c in txt)))
# attacker: knows N=97 and the PUBLIC order; reads digits of addr under public order -> substituted text
seen=pub.regenerate_text(addr)
print("attacker sees text of length",len(seen),"(true length",len(txt),")")
# frequency analysis: rank-match against a reference English-ish corpus (a different file)
ref=open('/home/rendier/Projects/ThePlace/VAPMIP/README.md',encoding='utf-8',errors='ignore').read()
ref=''.join(c for c in ref if c in pub._char_index)
rs=[c for c,_ in Counter(ref).most_common()]; ss=[c for c,_ in Counter(seen).most_common()]
guess={s:r for s,r in zip(ss,rs)}
truth={chars[perm.index(c)]:c for c in txt}
hit=sum(guess.get(k)==v for k,v in truth.items())
pos=sum(guess.get(a)==b for a,b in zip(seen,txt))/len(txt)
print(f"rank-matching alone: {hit}/{len(truth)} symbols right, {100*pos:.1f}% of positions recovered; keyspace 97! = 2^{math.log2(math.factorial(97)):.0f}")

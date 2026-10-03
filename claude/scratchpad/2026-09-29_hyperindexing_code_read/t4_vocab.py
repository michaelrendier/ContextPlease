"""T4: VocabFactorizer 'reduction_factor' vs total stored size (address + vocabulary + punctuation mask)."""
import importlib.util, math, json
p='/home/rendier/Projects/ThePlace/PtolemyDesktop/Callimachus/HyperWebster-Data-Storage/hyperwebster_manifold.py'
spec=importlib.util.spec_from_file_location('m',p); m=importlib.util.module_from_spec(spec); spec.loader.exec_module(m)
V=m.VocabFactorizer()
txt=open('/home/rendier/Projects/ThePlace/Ainulindale/README.md',encoding='utf-8',errors='ignore').read()
txt=''.join(c for c in txt if c in set(m._DEFAULT_CHARS))
for L in (47,1000,4000,20000):
    t=txt[:L]; va=V.encode(t); ok=V.decode(va)==t; r=va.bit_report(t)
    vocab_bits=sum(len(w)+1 for w in va.vocab)*math.log2(97)          # vocabulary listed as text, N=97
    punct_bits=sum(len(s)*math.log2(97)+math.log2(max(va.word_count,2)) for _,s in va.punct_mask)
    total=r['vocab_token_bits']+vocab_bits+punct_bits
    print(f"L={L}: round-trip {ok}; reported reduction {r['reduction_factor']}; naive {r['naive_char_bits']} bits; token-address {r['vocab_token_bits']}; "
          f"+vocab {vocab_bits:.0f} +punct {punct_bits:.0f} = {total:.0f} => real ratio {r['naive_char_bits']/total:.2f}x")

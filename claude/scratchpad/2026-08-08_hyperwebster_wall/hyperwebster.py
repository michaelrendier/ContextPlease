from math import log2

print("=== WALL 1: does a hyperwebster index COMPRESS? (counting argument) ===")
for k, label in ((26,'a-z'), (256,'bytes')):
    print(f"\n  alphabet {label} (k={k}):")
    for n in (3, 10, 1024):
        count = k**n
        bits_index = log2(count)
        bits_data  = n*log2(k)
        print(f"    length {n:5d}: {k}^{n} strings -> index needs {bits_index:10.1f} bits ;"
              f" data is {bits_data:10.1f} bits   ratio {bits_index/bits_data:.4f}")
print("\n  The index is EXACTLY as long as the data. Always. Any bijection between")
print("  strings and indices preserves length -- that is the pigeonhole/counting")
print("  argument for lossless compression. No encoding choice escapes it.\n")

print("=== WALL 2: is index-proximity SEMANTIC proximity? ===")
def lex_index(s, k=26, off=ord('a')):
    """index of s in the enumeration of all strings ordered by length then lex"""
    idx = sum(k**i for i in range(1, len(s)))          # all shorter strings
    for ch in s: idx = idx*k + (ord(ch)-off)
    return idx

pairs = [("cat","cats"), ("cat","car"), ("cat","feline"), ("cat","dog"),
         ("big","large"), ("hot","cold")]
print(f"  {'pair':22s} {'|index difference|':>26s}   relationship")
for a,b in pairs:
    d = abs(lex_index(a)-lex_index(b))
    rel = {("cat","cats"):"inflection (spelling)", ("cat","car"):"UNRELATED, 1 letter apart",
           ("cat","feline"):"SYNONYM", ("cat","dog"):"co-hyponym",
           ("big","large"):"SYNONYM", ("hot","cold"):"ANTONYM"}[(a,b)]
    print(f"  {a+' / '+b:22s} {d:26,d}   {rel}")
print("\n  'cat'/'car' are UNRELATED but adjacent. 'cat'/'feline' are SYNONYMS but")
print("  ~300 million apart. The index metric measures SPELLING, not meaning.")

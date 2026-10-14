"""Hearst-style (1992) pattern extraction of typed WordNet-relation candidates from ingested text. Regex over the raw sentences; NLTK only for the check against WordNet."""
import re
from nltk.corpus import wordnet as wn
txt=open('neutron_generation_overview.txt').read()
P=[('hyponyms',  r"(?P<h>[A-Za-z][\w -]{2,40}?) (?:like|such as|including) (?P<t>[A-Za-z][\w-]*(?:-\d+)?(?:, [A-Za-z][\w-]*(?:-\d+)?)*(?:,? (?:and|or) [A-Za-z][\w-]*)?)"),
   ('hyponyms',  r"(?P<t>[A-Z][\w -]{2,30}) (?:is|are) (?:a|an|the) (?P<h>[a-z][\w -]{2,30})"),
   ('part_meronyms', r"(?P<h>[a-z][\w -]{2,25}) (?:consists? of|contains?|includes?) (?P<t>[a-z][\w -]{2,25})"),
   ('causes',    r"(?P<h>[A-Za-z][\w -]{2,30}) (?:produces?|releases?|triggers?|causes?) (?P<t>[a-z][\w -]{2,30})"),
   ('also_sees', r"(?P<h>[A-Za-z][\w -]{2,30}) (?:refers to|is used (?:in|for)) (?P<t>[a-z][\w -]{2,30})")]
seen=set()
for sent in re.split(r'(?<=[.:])\s+',txt):
    for rel,pat in P:
        for m in re.finditer(pat,sent):
            h,t=m.group('h').strip(),m.group('t').strip()
            if (rel,h,t) in seen: continue
            seen.add((rel,h,t))
            hl=h.split()[-1].lower(); inwn=bool(wn.synsets(hl,'n'))
            print(f"{rel:13s} | {h[:34]:34s} -> {t[:44]:44s} | head '{hl}' in WordNet: {inwn}")

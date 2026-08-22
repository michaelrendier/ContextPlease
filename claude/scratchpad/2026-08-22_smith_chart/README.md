# The Smith chart — an independent Möbius/L_(I|O) confirmation, 2026-08-22

Cody named the Veritasium video "The Scariest Chart in Electrical Engineering"
(youtube.com/watch?v=GK2pZ_oVU1o, published 2026-07-14). Found via WebSearch;
YouTube page itself has no fetchable transcript (JS-rendered), so grounded via
summify.io's summary of the video plus independent verification of the
underlying mathematics in smith_chart_test.py.

The Smith chart (Phillip Smith, Bell Labs, 1939) is Gamma=(Z-Z0)/(Z+Z0) — a
Mobius transform. Verified exact: Z=Z0 is the unique fixed point (Gamma=0, the
matched anchor); Z=0/Z->inf (short/open) are the other two anchors, driven to
the boundary |Gamma|=1; |Gamma|=1 <=> Re(Z)=0 exactly (the lossless/reactive
locus = the horizon); constant-R/constant-X families orthogonal (conformal);
Y=1/Z (admittance, inside-out) is EXACTLY Gamma -> -Gamma, a pi-rotation on the
same chart.

Engine relation: SedenionFactoralRelativity/engine/lineage.py,
pathway.smith_chart_is_the_same_mobius (PW8), 36/36.

HONEST: not evidence FOR the wider framework -- an independent 90-year-old
existence proof that the mathematical shape (Mobius + fixed anchor + tunable
path between two anchors) is exactly what real engineering reaches for.

Sources:
- https://www.youtube.com/watch?v=GK2pZ_oVU1o
- https://summify.io/discover/the-scariest-chart-in-electrical-engineering-GK2pZ_

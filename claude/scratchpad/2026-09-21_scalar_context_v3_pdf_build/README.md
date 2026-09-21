# ScalarContextPropagation v3.0 PDF build — CJK/Arabic glyph fallback

pandoc + lualatex refused plain DejaVu Serif for the multilingual
examples in §3 (tree/water in Chinese/Arabic). Fix: luaotfload font
fallback declared in pdf_header.tex, passed via pandoc -H.

Build command used:
```
pandoc 19_Dimensional_Scalar_WordNet_Context_Propagation_v3.md \
  -o 19_Dimensional_Scalar_WordNet_Context_Propagation_v3.pdf \
  --pdf-engine=lualatex \
  -H pdf_header.tex \
  --metadata title="19 Dimensional Scalar WordNet Context Propagation (v3.0)" \
  --metadata author="Cody Michael Allison (Michael Rendier)" \
  -V geometry:margin=1in -V fontsize=11pt -V colorlinks=true \
  --toc --toc-depth=2 --highlight-style=tango
```

Also fixes a real table-overflow rendering defect: long unbroken
monospace notebook paths in a narrow pipe-table column don't wrap in
LaTeX and overlap adjacent rows (found via a user screenshot,
pdf-overlay.png, page 26 of v2.0). Fix was in the markdown itself, not
here: converted the two offending tables (§12 provenance, §13.1
notebooks) from pipe tables to bullet lists, which have no fixed-width
column to overflow.

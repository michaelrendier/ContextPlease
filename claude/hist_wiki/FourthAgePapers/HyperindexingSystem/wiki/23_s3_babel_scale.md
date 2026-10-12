# S3 · Library of Babel scale, computed

*Claude Sonnet 5.5, 2026-09-29. Notebook: [`w03_babel_scale/`](../notebooks/w03_babel_scale/).*

Premise cited under the paper's title: Basile, `libraryofbabel.info/About.html`: the site holds all pages of 3,200 characters ("approximately 10^4677 books"); the complete library would hold every combination of 1,312,000 characters. The site's own numbering algorithm is not examined here; the numbering below is this paper's, using the shipped class (v02) with a 29-symbol charset (26 letters, space, comma, period).

## The numbers

- 29³²⁰⁰ = 10^4679.67 pages of 3,200 characters; divided by 410 pages per book = **10^4677.06**, matching the site's 10^4677. 1,312,000 = 410 × 3,200 = 410 pages × 40 lines × 80 characters. Books of 1,312,000 characters: 10^1,918,666.
- A random page: 15,544 bits (log₂29 = 4.858 bits/char; 4.86 · 3,200 = 15,544), exact round trip, encode 213 ms, decode 17 ms; 0.607 of the page's size at 8 bits/char (= log₂29/8).

## Exact relations

- Among all strings the class ranks by length first; among the 3,200-character pages the location is the plain base-29 numeral of the page. The two differ by (29³²⁰⁰ − 29)/28, the number of shorter strings: verified on a random page.
- The first page (3,200 × `a`) has location 0 and the last (3,200 × `.`) has location 29³²⁰⁰ − 1.
- Neighbouring pages are neighbouring integers: changing the last character one step moves the location by exactly 1; changing the first moves it by 29³¹⁹⁹.

## One book

The address of a 1,312,000-character book is 6,373,671 bits (778 KiB). Encode time, fitted from 2,000 to 16,000 characters, extrapolated to a book (**estimates, not measured**):

| loop | fitted growth | one book |
|---|---:|---:|
| `point_to_text` (v02) | n^2.6 | about 151 h |
| forward Horner | n^1.8 | about 203 s |

The choice of loop is a factor of about 2,700 at this size. Both return the same integer (page 03).

"""Chase of the borderline rank-test cell (n=5, level 4, overflow guide): first run z=-2.0 (100 trials, seed 1); then three further seeds of 300 trials. Exact seeds, so reproducible.
Run:  python3 chase_borderline_cell.py   (needs MultiplicationMatrixExplorer next to ThePlace/ or EXPLORER_PATH)"""
import os, sys
sys.path.insert(0, os.environ.get('EXPLORER_PATH', os.path.join(os.path.dirname(os.path.abspath(__file__)), '..', '..', '..', '..', 'MultiplicationMatrixExplorer')))
from toolsets import torsor as T
for n, lv, tr, seed in ((4, 3, 60, 0), (4, 3, 400, 1), (4, 3, 400, 2), (5, 4, 100, 1), (5, 4, 300, 3), (5, 4, 300, 4), (5, 4, 300, 5)):
    r = T.rank_test(n, lv, trials=tr, seed=seed)
    print(n, lv, tr, seed, {g: round(v, 3) for g, v in r['mean_rank'].items()}, {g: round(v, 1) for g, v in r['z_vs_no_information'].items()})

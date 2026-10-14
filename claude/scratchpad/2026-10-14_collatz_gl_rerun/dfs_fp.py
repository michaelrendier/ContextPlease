import sys, time; sys.path.insert(0,'engine')
import e_collatz_bl_replication as bl
def odd_fixed_points_dfs(N):
    """Second, independent algorithm. For a fixed point x of Q_n the parity of T^j(x) must equal bit j of x. With T^j(x) = (3^d x + c)/2^j along the parity word
    (= the low bits of x), the parity of T^j(x) is f_j XOR x_j where f_j = ((3^d x_low + c)/2^j) mod 2 depends only on x_low (bits < j). So bit j is free if f_j = 0 and the branch dies if f_j = 1."""
    nodes = [(1, 1, 1, 1)]          # after choosing x_0 = 1 (odd): (x_low, d, c, bits) with step 0 taken: parity 1 -> c' = 3*0 + 2^0 = 1, d = 1
    counts = {1: 1}
    p3 = [1]
    for j in range(1, N):
        nxt = []
        for x_low, d, c, _ in nodes:
            # f_j needs 3^d * x_low + c, divisible by 2^j by construction
            val = (pow3(d) * x_low + c) >> j
            if val & 1: continue
            for b in (0, 1):
                if b == 0: nxt.append((x_low, d, c, j + 1))
                else: nxt.append((x_low | (1 << j), d + 1, 3 * c + (1 << j), j + 1))
        nodes = nxt
        counts[j + 1] = len(nodes)
    return counts
_p3 = [1]
def pow3(d):
    while len(_p3) <= d: _p3.append(_p3[-1] * 3)
    return _p3[d]
t = time.time(); dfs = odd_fixed_points_dfs(1000); print('DFS to n=1000 in %.1fs' % (time.time() - t))
fp = bl.odd_fixed_point_counts(100)
print('DFS == Q-based lineage for n=1..100:', all(dfs[n] == fp[n] for n in range(1, 101)))
print('differences vs printed Table 2.3 (n=2..100):', [n for n in range(2, 101) if dfs[n] != bl.TABLE_2_3[n]])
print('differences vs printed Table 2.4 (n=10,20,...,1000):', [n for n in sorted(bl.TABLE_2_4) if dfs[n] != bl.TABLE_2_4[n]])
print('n=66..78  DFS', [dfs[n] for n in range(66, 79)])

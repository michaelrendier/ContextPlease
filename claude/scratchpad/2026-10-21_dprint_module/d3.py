import threading, numpy as np
from fractions import Fraction
def gen(n):
    for i in range(n):
        yield i * i
def f():
    a = np.zeros((2, 2)); a[0, 1] = 3
    fr = Fraction(1, 3); fr = fr + 1
    big = list(range(1000)); big.append(1)
    s = sum(gen(3))
    cyc = []; cyc.append(cyc)
    t = threading.Thread(target=lambda: None); t.start(); t.join()
    try:
        1 / 0
    except ZeroDivisionError as e:
        err = e
    return s
f()

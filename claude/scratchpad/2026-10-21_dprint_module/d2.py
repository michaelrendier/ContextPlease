import DPrint as DP
DP.flag = 1
@DP.watch
def f(a):
    b = a * 2
    b += 1
    return b
def g(x):
    y = x + 1
    return y
f(3); g(1)
with DP.watch():
    z = [1, 2]
    z.append(3)
    w = g(5)
print("flag", DP.flag)
DP.flag = 0
f(9)

import DPrint as DP

class Base:
    def __init__(self, name):
        self.name = name
        self.parent = None

class Leaf(Base):
    def __init__(self, name, parent):
        super().__init__(name)
        self.parent = parent
        self.count = 0

    def bump(self, n):
        for i in range(n):
            self.count += i
        return self.count

def work():
    grid = [[0, 0], [0, 0]]
    total = 0
    grid[1][0] = 7
    total = total + grid[1][0]
    root = Base("root")
    leaf = Leaf("leaf", root)
    leaf.bump(3)
    zero = 0
    DP.print(total, zero, "")
    DP.print("TABLE", grid)
    DP.print(leaf)
    return total

work()

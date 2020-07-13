class WeightedQuickUnion:
    def __init__(self, size):
        self.ids = [*range(size)]
        self.sizes = [1] * len(self.ids)

    def __root(self, i):
        while (i != self.ids[i]):
            i = self.ids[i]
        return i

    def union(self, p, q):
        p_root = self.__root(p)
        q_root = self.__root(q)
        if p_root == q_root:
            return
        if self.sizes[p] > self.sizes[q]:
            self.ids[p_root] = q_root
            self.sizes[q] += self.sizes[p]
        else:
            self.ids[q_root] = p_root
            self.sizes[p] += self.sizes[q]

    def connected(self, p, q):
        return self.__root(q) == self.__root(p)


uf = WeightedQuickUnion(10)

uf.union(4, 3)
uf.union(3, 8)
uf.union(6, 5)
uf.union(9, 4)
uf.union(2, 1)
uf.union(8, 9)

print(uf.connected(5, 4))  # False

uf.union(5, 0)
uf.union(7, 2)
uf.union(6, 1)
uf.union(7, 3)

print(uf.connected(5, 4))  # True

class QuickFind:
    def __init__(self, elements):
        self.ids = elements

    def union(self, p, q):
        pid = self.ids[p]
        qid = self.ids[q]
        self.ids[q] = p
        for i, v in enumerate(self.ids):
            if v == qid:
                self.ids[i] = pid

    def connected(self, p, q):
        return self.ids[p] == self.ids[q]


uf = QuickFind([*range(10)])

uf.union(1, 5)
uf.union(5, 9)

print(uf.ids)

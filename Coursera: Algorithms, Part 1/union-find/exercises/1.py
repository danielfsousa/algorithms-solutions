'''
Social network connectivity. Given a social network containing n members
and a log file containing m timestamps
at which times pairs of members formed friendships,
design an algorithm to determine the earliest time at which all members are connected
(i.e., every member is a friend of a friend of a friend ... of a friend).
Assume that the log file is sorted by timestamp
and that friendship is an equivalence relation.
The running time of your algorithm should be m log⁡ n
or better and use extra space proportional to n.
'''


logs = [(0, 1, '2015-08-14 18:00:00'),
        (1, 9, '2015-08-14 18:01:00'),
        (0, 2, '2015-08-14 18:02:00'),
        (0, 3, '2015-08-14 18:04:00'),
        (0, 4, '2015-08-14 18:06:00'),
        (0, 5, '2015-08-14 18:08:00'),
        (0, 6, '2015-08-14 18:10:00'),
        (0, 7, '2015-08-14 18:12:00'),
        (0, 8, '2015-08-14 18:14:00'),
        (1, 2, '2015-08-14 18:16:00'),
        (1, 3, '2015-08-14 18:18:00'),
        (1, 4, '2015-08-14 18:20:00'),
        (1, 5, '2015-08-14 18:22:00'),
        (2, 1, '2015-08-14 18:24:00'),
        (2, 3, '2015-08-14 18:26:00'),
        (2, 4, '2015-08-14 18:28:00'),
        (5, 5, '2015-08-14 18:30:00'),
        (7, 8, '2015-08-14 18:32:00'),
        (0, 8, '2015-08-14 18:32:00'),
        (0, 4, '2015-08-14 18:32:00')]


class WeightedQuickUnionPathCompression:
    def __init__(self, size):
        self.ids = [*range(size)]
        self.sizes = [1] * size
        self.connections = size

    def __root(self, i):
        while (i != self.ids[i]):
            self.ids[i] = self.ids[self.ids[i]]
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
        self.connections -= 1

    def connected(self, p, q):
        return self.__root(p) == self.__root(q)

    def _connections():
        return


uf = WeightedQuickUnionPathCompression(10)
for p, q, timestamp in logs:
    uf.union(p, q)
    if uf.connections == 1:
        print(f"found: {timestamp}")
        print(uf.ids)
        break

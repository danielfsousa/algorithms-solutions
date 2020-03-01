'''
Successor with delete. Given a set of n integers S={0,1,...,n−1} and a sequence of requests of the following form:

   Remove x from S
   Find the successor of x: the smallest y in S such that y≥x.

design a data type so that all operations (except construction) take logarithmic time or better in the worst case.
'''


class QuickUnionLargestElement:
    def __init__(self, size):
        self.ids = [*range(size)]
        self.sizes = [1] * len(self.ids)
        self.largest_elements = [*range(size)]

    def __root(self, i):
        while (i != self.ids[i]):
            self.ids[i] = self.ids[self.ids[i]]
            i = self.ids[i]
        return i

    def union(self, p, q):
        p_root = self.__root(p)
        q_root = self.__root(q)
        largest_element = max(self.largest_elements[p_root], self.largest_elements[q_root])

        if self.largest_elements[p_root] > p:
            self.largest_elements[p] = self.largest_elements[p_root]
        else:
            self.largest_elements[p_root] = self.largest_elements[p_root]

        if p_root == q_root:
            return

        if self.sizes[p] > self.sizes[q]:
            self.ids[p_root] = q_root
            self.sizes[q] += self.sizes[p]
            self.largest_elements[q_root] = largest_element
        else:
            self.ids[q_root] = p_root
            self.sizes[p] += self.sizes[q]
            self.largest_elements[p_root] = largest_element

    def find(self, i):
        return self.largest_elements[self.__root(i)]

    def connected(self, p, q):
        return self.__root(q) == self.__root(p)


class SuccessorWithDelete:
    def __init__(self, size):
        self.size = size
        self.uf = QuickUnionLargestElement(size)
        self.removed = [False for x in range(size)]

    def remove(self, i):
        self.removed[i] = True
        if i > 0 and self.removed[i - 1]:
            self.uf.union(i, i - 1)
        if i < self.size - 1 and self.removed[i + 1]:
            self.uf.union(i, i + 1)

    def successor(self, i):
        if not self.removed[i]:
            return i
        else:
            res = self.uf.find(i) + 1
            if res >= self.size:
                return -1
            return res


test = SuccessorWithDelete(10)
test.remove(2)
print(test.successor(2) == 3)
test.remove(3)
print(test.successor(2) == 4)
print(test.successor(8) == 8)
test.remove(8)
print(test.successor(8) == 9)
test.remove(9)
print(test.successor(8) == -1)
test.remove(5)
test.remove(4)
print(test.successor(3) == 6)

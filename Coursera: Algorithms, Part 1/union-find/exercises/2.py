'''
Union-find with specific canonical element.
Add a method find() to the union-find data type so that
find(i) returns the largest element in the connected component containing i.
The operations, union(), connected(), and find() should all take logarithmic time or better.

For example, if one of the connected components is {1,2,6,9},
then the find() method should return 9
for each of the four elements in the connected components.
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


# === START ===

uf = QuickUnionLargestElement(10)

uf.union(1, 2)
uf.union(6, 1)
uf.union(2, 9)

print(uf.find(1))  # 9
print(uf.find(2))  # 9
print(uf.find(6))  # 9
print(uf.find(9))  # 9

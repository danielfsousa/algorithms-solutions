# https://www.hackerrank.com/challenges/swap-nodes-algo/problem

import os
import sys
from collections import deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def swap(self):
        self.left, self.right = self.right, self.left


class Tree:
    def __init__(self, indexes):
        self.root = Node(1)
        queue = deque([self.root])
        i = 0
        while queue:
            node = queue.popleft()
            left, right = indexes[i]
            node.left = Node(left) if left != -1 else None
            node.right = Node(right) if right != -1 else None
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
            i += 1

    def swap(self, k):
        return 0

    def in_order_recursive(self):
        sys.setrecursionlimit(10000)

        def recur(node):
            if not node:
                return []
            return recur(node.left) + [node.data] + recur(node.right)
        return recur(self.root)

    def in_order(self):
        ordered = []
        stack = deque()
        node = self.root
        while True:
            if node:
                stack.append(node)
                node = node.left
            elif stack:
                node = stack.pop()
                ordered.append(node.data)
                node = node.right
            else:
                break
        return ordered

        def recur(node):
            if not node:
                return []
            return recur(node.left) + [node.data] + recur(node.right)
        return recur(self.root)


def is_multiple(a, b):
    return a % b == 0


#
# Complete the swapNodes function below.
#
def swapNodes(indexes, queries):
    tree = Tree(indexes)
    results = []

    for k in queries:
        height = 1
        nodes = []
        queue = deque([tree.root])
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                queue += filter(None, (node.left, node.right))
                if is_multiple(height, k):
                    node.swap()
            height += 1
        results.append(tree.in_order())
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    indexes = []

    for _ in range(n):
        indexes.append(list(map(int, input().rstrip().split())))

    queries_count = int(input())

    queries = []

    for _ in range(queries_count):
        queries_item = int(input())
        queries.append(queries_item)

    result = swapNodes(indexes, queries)

    fptr.write('\n'.join([' '.join(map(str, x)) for x in result]))
    fptr.write('\n')

    fptr.close()

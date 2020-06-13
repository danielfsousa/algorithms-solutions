# https://www.hackerrank.com/challenges/tree-level-order-traversal/problem

from collections import deque

def levelOrder(root):
    """
    BFS

    v = Vertices
    e = Edges

    Time complexity:   O(v + e)
    Space complexity:  O(v)
    """
    search_queue = deque()
    search_queue.append(root)
    level_order = []

    while search_queue:
        node = search_queue.popleft()
        if node.info:
            level_order.append(str(node.info))
        if node.left:
            search_queue.append(node.left)
        if node.right:
            search_queue.append(node.right)

    print(' '.join(level_order))


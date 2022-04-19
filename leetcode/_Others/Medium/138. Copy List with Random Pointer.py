# https://leetcode.com/problems/copy-list-with-random-pointer/

from collections import defaultdict


# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    def copyRandomList(self, head: 'Node') -> 'Node':
        """
        Time complexity:  O(n)
        Space complexity: O(n)
        """
        nodes = defaultdict(lambda: Node(0))
        nodes[None] = None
        n = head

        while n:
            nodes[n].val = n.val
            nodes[n].next = nodes[n.next]
            nodes[n].random = nodes[n.random]
            n = n.next

        return nodes[head]

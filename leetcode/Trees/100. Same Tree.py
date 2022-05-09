# https://leetcode.com/problems/same-tree/

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        """
        Recursive DFS

        Time complexity:  O(min(p, q)) == O(n)
        Space complexity: O(min(p, q)) == O(n)
        """
        if not p and not q:
            return True

        if not p or not q:
            return False

        curr_is_same = p.val == q.val
        left_is_same = self.isSameTree(p.left, q.left)
        right_is_same = self.isSameTree(p.right, q.right)

        return curr_is_same and left_is_same and right_is_same

    def isSameTreeIterativeDFS(
        self, p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> bool:
        """
        Iterative DFS

        Time complexity:  O(min(p, q)) == O(n)
        Space complexity: O(min(p, q)) == O(n)
        """
        stack = deque([(p, q)])
        while stack:
            node1, node2 = stack.pop()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                stack.append((node1.left, node2.left))
                stack.append((node1.right, node2.right))
            elif not node1 and not node2:
                continue
            else:
                return False

        return True

    def isSameTreeIterativeBFS(
        self, p: Optional[TreeNode], q: Optional[TreeNode]
    ) -> bool:
        """
        Iterative BFS

        Time complexity:  O(min(p, q)) == O(n)
        Space complexity: O(min(p, q)) == O(n)
        """
        queue = deque([(p, q)])
        while queue:
            node1, node2 = queue.popleft()
            if node1 and node2:
                if node1.val != node2.val:
                    return False
                queue.append((node1.left, node2.left))
                queue.append((node1.right, node2.right))
            elif not node1 and not node2:
                continue
            else:
                return False

        return True

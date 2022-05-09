# https://leetcode.com/problems/kth-smallest-element-in-a-bst/

# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        """
        Recursive DFS

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        res = None

        def dfs(node):
            nonlocal k, res
            if not node or k == 0:
                return

            dfs(node.left)

            k -= 1
            if k == 0:
                res = node.val
                return

            dfs(node.right)

        dfs(root)
        return res

    def kthSmallestIterative(self, root: Optional[TreeNode], k: int) -> int:
        """
        Iterative DFS

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        stack = []
        cur = root
        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left

            node = stack.pop()

            k -= 1
            if k == 0:
                return node.val

            cur = node.right

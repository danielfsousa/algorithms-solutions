# https://leetcode.com/problems/validate-binary-search-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        """
        DFS

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        def dfs(node, left, right):
            if not node:
                return True
            if not (node.val > left and node.val < right):
                return False

            return dfs(node.left, left, node.val) and dfs(node.right, node.val, right)

        return dfs(root, float("-inf"), float("inf"))

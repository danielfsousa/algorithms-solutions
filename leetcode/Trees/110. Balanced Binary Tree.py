# https://leetcode.com/problems/balanced-binary-tree/

from typing import NamedTuple, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Result(NamedTuple):
    is_balanced: bool
    height: int


class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        """
        Recursive DFS

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        def dfs(node):
            if not node:
                return Result(is_balanced=True, height=0)

            left, right = dfs(node.left), dfs(node.right)
            curr_is_balanced = abs(left.height - right.height) <= 1

            return Result(
                is_balanced=left.is_balanced and right.is_balanced and curr_is_balanced,
                height=max(left.height, right.height) + 1,
            )

        return dfs(root).is_balanced

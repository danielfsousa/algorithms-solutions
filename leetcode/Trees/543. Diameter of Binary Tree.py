# https://leetcode.com/problems/diameter-of-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        """
        DFS

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        diameter = 0

        def height(node):
            nonlocal diameter
            # define the height of an empty tree to be -1.
            if not node:
                return -1

            left_height = height(node.left)
            right_height = height(node.right)

            # the "2+" accounts for the edge on the left plus the edge on the right.
            diameter = max(diameter, 2 + left_height + right_height)

            return 1 + max(left_height, right_height)

        height(root)
        return diameter

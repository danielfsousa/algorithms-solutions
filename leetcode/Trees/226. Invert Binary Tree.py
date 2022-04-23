# https://leetcode.com/problems/invert-binary-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        """
        Depth first search

        n = number of nodes

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        if root:
            root.left, root.right = root.right, root.left
            self.invertTree(root.left)
            self.invertTree(root.right)
        return root


# test
#
# input
#
#       4
#     /  \
#   2     7
#  / \   / \
# 1   3 6   9
#
# output
#
#       4
#     /  \
#   7     2
#  / \   / \
# 9   6 3   1

head = TreeNode()

print(Solution().invertTree(head))

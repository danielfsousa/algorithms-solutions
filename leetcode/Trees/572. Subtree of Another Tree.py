# https://leetcode.com/problems/subtree-of-another-tree/

from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        """
        For each subtree check if is the same tree

        Time complexity:  O(n * m)  - n = first tree, m = second tree
        Space complexity: O(n)      - n = height of first tree
        """
        if not subRoot:
            return True
        if not root:
            return False

        return (
            self.isSameTree(root, subRoot)
            or self.isSubtree(root.left, subRoot)
            or self.isSubtree(root.right, subRoot)
        )

    def isSameTree(self, q, p):
        if not q and not p:
            return True
        if not q or not p:
            return False

        is_cur_same = q.val == p.val
        is_left_same = self.isSameTree(q.left, p.left)
        is_right_same = self.isSameTree(q.right, p.right)

        return is_cur_same and is_left_same and is_right_same

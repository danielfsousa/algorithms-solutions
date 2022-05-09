# https://leetcode.com/problems/count-good-nodes-in-binary-tree/

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        """
        DFS

        Time complexity:  O(n)
        Space complexity: O(n) - n = height of the tree
        """
        total = 0

        def dfs(node, max_val):
            nonlocal total
            if not node:
                return

            if node.val >= max_val:
                total += 1

            max_val = max(max_val, node.val)
            dfs(node.left, max_val)
            dfs(node.right, max_val)

        dfs(root, -float("inf"))
        return total

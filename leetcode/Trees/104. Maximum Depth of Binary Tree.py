# https://leetcode.com/problems/maximum-depth-of-binary-tree/

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        """
        Recursive DFS

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        if not root:
            return 0

        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))

    def maxDepthIterativeDFS(self, root: Optional[TreeNode]) -> int:
        """
        Iterative DFS

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        max_depth = 0
        stack = deque([(root, 0)])

        while stack:
            node, depth = stack.pop()
            max_depth = max(max_depth, depth)

            if node:
                stack.append((node.left, depth + 1))
                stack.append((node.right, depth + 1))

        return max_depth

    def maxDepthIterativeBFS(self, root: Optional[TreeNode]) -> int:
        """
        Iterative BFS

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        if not root:
            return 0

        max_depth = 0
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            max_depth += 1

        return max_depth

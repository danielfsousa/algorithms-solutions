from collections import deque


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root) -> int:
        """
        BFS approach

        v = Vertices
        e = Edges
        d = Depth

        Time complexity:   O(v + e)
        Space complexity:  O(v)
        """
        if not root:
            return 0

        depth = 1
        queue = deque([root])

        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if not node.left and not node.right:
                    return depth
                else:
                    queue += filter(None, (node.left, node.right))
            depth += 1

        return depth

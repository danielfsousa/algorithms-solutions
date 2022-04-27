from collections import deque
from typing import List


class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        """
        Breadth First Search

        r = rows
        c = cols

        Time complexity:  O(r * c)
        Space complexity: O(r * c)
        """
        rows, cols = len(mat), len(mat[0])
        dirs = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        visited = set()
        queue = deque()

        for row in range(rows):
            for col in range(cols):
                if mat[row][col] == 0:
                    visited.add((row, col))
                    queue.append((row, col))

        while queue:
            row, col = queue.popleft()
            for rowdir, coldir in dirs:
                curr_row, curr_col = row + rowdir, col + coldir
                is_in_bounds = 0 <= curr_row < rows and 0 <= curr_col < cols
                has_visited = (curr_row, curr_col) in visited
                if is_in_bounds and not has_visited:
                    mat[curr_row][curr_col] = mat[row][col] + 1
                    visited.add((curr_row, curr_col))
                    queue.append((curr_row, curr_col))

        return mat

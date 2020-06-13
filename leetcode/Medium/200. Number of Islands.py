# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    """
    Recursively DFS

    n = rows
    m = cols
    d = depth

    Time Complexity:  O(n * m)
    Space Complexity: O(d)
    """
    def change_visited(self, grid, row, col):
        """
        change visited clusters to 0
        """
        out_of_bounds = row < 0 or row >= len(
            grid) or col < 0 or col >= len(grid[row])
        if out_of_bounds or grid[row][col] == '0':
            return
        grid[row][col] = '0'
        self.change_visited(grid, row + 1, col)
        self.change_visited(grid, row - 1, col)
        self.change_visited(grid, row, col - 1)
        self.change_visited(grid, row, col + 1)

    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        rows = len(grid)
        cols = len(grid[0])
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    count += 1
                    self.change_visited(grid, int(row), int(col))
        return count

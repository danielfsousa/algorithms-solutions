# https://leetcode.com/problems/number-of-islands/

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """
        Depth first search

        r = number of rows
        c = number of columns

        Time complexity:  O(r * c)
        Space complexity: O(r * c)
        """
        rows, cols = len(grid), len(grid[0])
        visited = set()

        def has_island(row, col):
            is_in_bounds = 0 <= row < rows and 0 <= col < cols
            has_visited = (row, col) in visited

            if is_in_bounds and not has_visited and grid[row][col] == "1":
                visited.add((row, col))
                has_island(row - 1, col)
                has_island(row + 1, col)
                has_island(row, col - 1)
                has_island(row, col + 1)
                return True

            return False

        count = 0
        for row in range(rows):
            for col in range(cols):
                if has_island(row, col):
                    count += 1

        return count

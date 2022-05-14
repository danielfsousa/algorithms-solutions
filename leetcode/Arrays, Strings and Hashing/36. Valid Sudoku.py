# https://leetcode.com/problems/valid-sudoku/

from collections import defaultdict
from typing import List


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        """
        Keep a hash set cache for row, column and 3x3 grid

        Time complexity:  O(9^2)
        Space complexity: O(9^2)
        """
        rows_cache = defaultdict(set)
        cols_cache = defaultdict(set)
        grid_cache = defaultdict(set)

        for row in range(9):
            for col in range(9):
                cell = board[row][col]
                if cell == ".":
                    continue

                grid_key = f"{row // 3}_{col // 3}"

                if (
                    cell in rows_cache[row]
                    or cell in cols_cache[col]
                    or cell in grid_cache[grid_key]
                ):
                    return False

                rows_cache[row].add(cell)
                cols_cache[col].add(cell)
                grid_cache[grid_key].add(cell)
        return True

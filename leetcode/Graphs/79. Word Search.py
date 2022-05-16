# https://leetcode.com/problems/word-search/

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        """
        DFS backtracking

        n = rows
        m = cols
        w = word length

        Time complexity:  O(n * m * 4^w)
        Space complexity: O(n * m)
        """
        rows, cols = len(board), len(board[0])
        seen = set()

        def has_word(row, col, word_idx):
            is_in_bounds = 0 <= row < rows and 0 <= col < cols

            if word_idx == len(word):
                return True

            if (
                not is_in_bounds
                or (row, col) in seen
                or word[word_idx] != board[row][col]
            ):
                return False

            next_word_idx = word_idx + 1
            seen.add((row, col))
            res = (
                has_word(row - 1, col, next_word_idx)
                or has_word(row + 1, col, next_word_idx)
                or has_word(row, col - 1, next_word_idx)
                or has_word(row, col + 1, next_word_idx)
            )
            seen.remove((row, col))
            return res

        for row in range(rows):
            for col in range(cols):
                if has_word(row, col, 0):
                    return True

        return False

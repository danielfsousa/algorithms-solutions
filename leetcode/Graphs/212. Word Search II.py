# https://leetcode.com/problems/word-search-ii/

from typing import List


class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_word = False


class Trie:
    def __init__(self, words):
        self.root = TrieNode()
        self.words_length = 0
        for word in words:
            self.insert(word)
            self.words_length += 1

    def __len__(self):
        return self.words_length

    def insert(self, word):
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.is_word = True


class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        """
        DFS backtracking to traverse the grid
        Trie to search words

        n = rows
        m = cols
        4 = directions
        l = longest word

        Time complexity:  O(n * m * 4^l)
        Space complexity: O(n * m)
        """
        rows, cols = len(board), len(board[0])
        trie = Trie(words)
        result = []

        def search_words(row, col, node, word):
            if len(trie) == 0:
                return

            is_in_bounds = 0 <= row < rows and 0 <= col < cols
            if not is_in_bounds or board[row][col] not in node.children:
                return

            cur_letter = board[row][col]
            board[row][col] = "#"

            word += cur_letter
            node = node.children[cur_letter]

            if node.is_word:
                result.append(word)
                node.is_word = False
                trie.words_length -= 1

            search_words(row - 1, col, node, word)
            search_words(row + 1, col, node, word)
            search_words(row, col - 1, node, word)
            search_words(row, col + 1, node, word)

            board[row][col] = cur_letter

        for row in range(rows):
            for col in range(cols):
                search_words(row, col, trie.root, "")

        return result

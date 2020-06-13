from typing import List, Tuple
from collections import defaultdict


class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = defaultdict()
        # Is it the last character of the word.`
        self.is_leaf = False
        # How many times this character appeared in the addition process
        self.counter = 1


class Trie:
    """
    A trie, sometimes called a radix or prefix tree, is a kind of search tree
    that is used to store a dynamic set or associative array where the keys are
    usually Strings. No node in the tree stores the key associated with that
    node; instead, its position in the tree defines the key with which it is
    associated. All the descendants of a node have a common prefix of the
    String associated with that node, and the root is associated with
    the empty String.

    ALPHABET_SIZE = Number of alphabets. Usually 26
    k = Length of key
    n = Number of keys in the trie

    Time complexity:
        Searching: O(k)
        Insertion: O(k)
        Deletion:
    Space Complexity: O(ALPHABET_SIZE * k * n)
    """

    def __init__(self, words: List[str]):
        self.root = TrieNode('*')
        for word in words:
            self.add(word)

    def get_index(self, char: str) -> int:
        return ord(char) - ord('a')

    def add(self, word: str):
        node = self.root
        for char in word:
            index = self.get_index(char)
            if index not in node.children:
                node.children[index] = TrieNode(char)
            else:
                node.children[index].counter += 1
            node = node.children.get(index)
        node.is_leaf = True

    def remove(self, word: str) -> bool:
        node = self.root
        for char in word:
            index = self.get_index(char)
            if not node:
                return False
            node = node.children.get(index)
        if not node:
            return False
        node.is_leaf = False
        return True

    def search(self, prefix: str) -> Tuple[bool, int]:
        """
        Check and return
            1. If the prefix exsists in any of the words we added so far
            2. If yes then how may words actually have the prefix
        """
        node = self.root
        for char in prefix:
            index = self.get_index(char)
            if not node:
                return False, 0
            node = node.children.get(index)
        if not node:
            return False, 0
        else:
            return node.is_leaf, node.counter

# test
# trie = Trie(['the', 'their', 'there', 'any', 'answer', 'by', 'bye'])
# trie.add('and')
# trie.add('andy')
# print(trie.search('and'))

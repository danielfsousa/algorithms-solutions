# https://www.hackerrank.com/challenges/contacts/problem

import os
import sys
from typing import Tuple
from collections import defaultdict

class TrieNode:
    def __init__(self, char: str):
        self.char = char
        self.children = defaultdict()
        self.is_leaf = False
        self.counter = 1


class Trie:
    def __init__(self):
        self.root = TrieNode('*')

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

    def search(self, prefix: str) -> Tuple[bool, int]:
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

#
# Complete the contacts function below.
#
def contacts(queries):
    trie = Trie()
    counts = []

    for query in queries:
        operation, name = query
        if operation == 'add':
            trie.add(name)
        elif operation == 'find':
            is_word, count = trie.search(name)
            counts.append(count)

    return counts

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    queries_rows = int(input())

    queries = []

    for _ in range(queries_rows):
        queries.append(input().rstrip().split())

    result = contacts(queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()

# https://leetcode.com/problems/implement-trie-prefix-tree/

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Time complexity:  O(n) - n = length of word
        Space complexity: O(n)
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                cur.children[char] = TrieNode()
            cur = cur.children[char]
        cur.isEndOfWord = True

    def search(self, word: str) -> bool:
        """
        Time complexity:  O(n) - n = length of word
        Space complexity: O(1)
        """
        cur = self.root
        for char in word:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return cur.isEndOfWord

    def startsWith(self, prefix: str) -> bool:
        """
        Time complexity:  O(n) - n = length of prefix
        Space complexity: O(1)
        """
        cur = self.root
        for char in prefix:
            if char not in cur.children:
                return False
            cur = cur.children[char]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

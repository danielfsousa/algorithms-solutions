# https://leetcode.com/problems/lru-cache/


class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:
    """
    Uses a dictionary to cache nodes
    and a doubly linked list to keep track of the least used nodes

    Time complexity:  O(1)
    Space complexity: O(n)
    """

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = dict()
        self.head = Node(0, 0)
        self.tail = Node(0, 0)
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1

        self._remove(node)
        self._add(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)

        if node:
            self._remove(node)
            node.val = value
            self._add(node)
            return

        if len(self.cache) == self.capacity:
            tail = self.tail.prev
            self._remove(tail)
            del self.cache[tail.key]

        node = Node(key, value)
        self._add(node)
        self.cache[key] = node

    def _add(self, node):
        next_node = self.head.next
        prev_node = self.head

        next_node.prev = node
        prev_node.next = node

        node.prev = prev_node
        node.next = next_node

    def _remove(self, node):
        prev_node = node.prev
        next_node = node.next

        prev_node.next = next_node
        next_node.prev = prev_node


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

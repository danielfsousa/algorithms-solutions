# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq
from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        """
        Time complexity:  O(n log n)
        Space complexity: O(1)
        """
        self.k = k
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        while len(self.min_heap) > self.k:
            heapq.heappop(self.min_heap)

    def add(self, val: int) -> int:
        """
        Time complexity:  O(log n)
        Space complexity: O(1)
        """
        if len(self.min_heap) < self.k:
            heapq.heappush(self.min_heap, val)
        else:
            heapq.heappushpop(self.min_heap, val)
        return self.min_heap[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

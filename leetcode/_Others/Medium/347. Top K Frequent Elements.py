# https://leetcode.com/problems/top-k-frequent-elements/

from typing import List
from itertools import chain
from heapq import heappush, heappushpop
from collections import Counter


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Counter approach

        Time complexity:  O(n log k)
        Space complexity: O(n)
        """
        return [x[0] for x in Counter(nums).most_common(k)]

    def topKFrequentHeap(self, nums: List[int], k: int) -> List[int]:
        """
        Max heap approach

        k = k most frequent elements

        Time complexity:  O(n log k)
        Space complexity: O(n)
        """
        heap = []

        for num, freq in Counter(nums).items():
            if len(heap) == k:
                heappushpop(heap, (freq, num))
            else:
                heappush(heap, (freq, num))

        return [x[1] for x in heap]

    def topKFrequentBucketSort(self, nums: List[int], k: int) -> List[int]:
        """
        Bucket sort approach

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        buckets = [[] for _ in nums]
        for num, freq in Counter(nums).items():
            buckets[-freq].append(num)
        return list(chain.from_iterable(buckets))[:k]

    def topKFrequentQuickSelect(self, nums: List[int], k: int) -> List[int]:
        """
        TODO: Quick select approach

        Time complexity:  O(n) average / O(n^2) worst
        Space complexity: O(1)
        """
        return []

# https://leetcode.com/problems/kth-largest-element-in-an-array/

from typing import List
from random import shuffle
from heapq import nlargest


class SolutionHeap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Heap approach

        Time complexity:  O(n log k)
        Space complexity: O(k)
        """
        return nlargest(k, nums).pop()


class SolutionQuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        QuickSelect approach

        Time complexity:  O(n) amortized / O(n^2) worst case
        Space complexity: O(1)
        """
        shuffle(nums)  # we shuffle to get a O(n) in the average case
        return self.quick_select(nums, len(nums) - k)

    def quick_select(self, arr, num) -> int:
        low = 0
        high = len(arr) - 1
        while low < high:
            partition = self.partition(arr, low, high)
            if partition < num:
                low = partition + 1
            elif partition > num:
                high = partition - 1
            else:
                break
        return arr[num]

    def partition(self, arr, low, high) -> int:
        i = low
        j = high
        while True:
            # find item on left to swap
            while arr[i] <= arr[low]:
                i += 1
                if i == high:
                    break
            # find item on right to swap
            while arr[low] <= arr[j]:
                j -= 1
                if j == low:
                    break
            # stop if pointers cross
            if i >= j:
                break
            # swap
            arr[i], arr[j], arr[j], arr[i]
        # swap with partitioning item
        arr[low], arr[j], arr[j], arr[low]
        return j

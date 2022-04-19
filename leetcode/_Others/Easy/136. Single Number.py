# https://leetcode.com/problems/single-number/

from typing import List
from collections import Counter
from functools import reduce
import operator


class Solution:
    def singleNumbers(self, nums: List[int]) -> int:
        """
        reduce XOR approach

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        return reduce(operator.xor, nums)

    def singleNumberSet(self, nums: List[int]) -> int:
        """
        set approach

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        seen = set()
        for num in nums:
            if num in seen:
                seen.remove(num)
            else:
                seen.add(num)
        return seen.pop()

    def singleNumberCounter(self, nums: List[int]) -> int:
        """
        Counter approach

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        counter = Counter(nums)
        for key, val in counter.items():
            if val < 2:
                return key
        return -1

    def singleNumberXOR(self, nums: List[int]) -> int:
        """
        XOR approach

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        result = 0
        for num in nums:
            result ^= num
        return result

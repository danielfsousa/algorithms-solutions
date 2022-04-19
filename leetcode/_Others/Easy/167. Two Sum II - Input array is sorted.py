# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int):
        """
        Two pointers approach

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        i = 0
        j = len(numbers) - 1

        while i < j:
            current_sum = numbers[i] + numbers[j]
            if current_sum == target:
                return i + 1, j + 1
            elif current_sum < target:
                i += 1
            else:
                j -= 1

    def twoSumDictionary(self, numbers: List[int], target: int):
        """
        Dictionary approach

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        numbers_dict = dict()

        for i in range(len(numbers) - 1, -1, -1):
            num = numbers[i]
            wanted = target - num
            found = numbers_dict.get(wanted)
            if found is not None:
                return i + 1, found + 1
            else:
                numbers_dict[num] = i

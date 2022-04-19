# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two pointers

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left + 1, right + 1]
            if res < target:
                left += 1
            else:
                right -= 1
        return []


# === tests ===

print(Solution().twoSum([2, 7, 11, 15], 9))  # [1,2]

# https://leetcode.com/problems/binary-search/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Binary search

        Time complexity:  O(log n)
        Space complexity: O(1)
        """
        left, right = 0, len(nums) - 1
        while left <= right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return mid
            if nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        return -1


# test
#
# input
#
# nums   = [1, 5, 7, 9]
# target = 7
#
# output = 2

print(Solution().search([1, 5, 7, 9], 7))  # 2

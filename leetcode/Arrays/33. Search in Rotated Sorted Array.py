# https://leetcode.com/problems/search-in-rotated-sorted-array/

from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """
        Custom binary search

        At most two sorted halfs, mid will be apart of left sorted or right sorted.
        If target is in range of sorted portion then search it,
        otherwise search other half.

        Time complexity:  O(log n)
        Space complexity: O(1)
        """
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid

            # left sorted half
            if nums[left] <= nums[mid]:
                if target >= nums[mid] or target < nums[left]:
                    left = mid + 1
                else:
                    right = mid - 1

            # right sorted half
            else:
                if target <= nums[mid] or target > nums[right]:
                    right = mid - 1
                else:
                    left = mid + 1

        return -1


# === tests ===

print(Solution().search([4, 5, 6, 7, 0, 1, 2]))  # 4

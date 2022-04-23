# https://leetcode.com/problems/container-with-most-water/

from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two pointers

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(height) - 1
        max_area = 0

        while left < right:
            min_height = min(height[left], height[right])
            width = right - left
            area = min_height * width
            max_area = max(max_area, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area


# test

print(Solution().maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))  # 49

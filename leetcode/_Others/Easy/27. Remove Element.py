# https://leetcode.com/problems/remove-element/

from typing import List


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        """
        Two pointers approach

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        index = 0
        for num in nums:
            if num != val:
                nums[index] = num
                index += 1
        return index

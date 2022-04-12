# https://leetcode.com/problems/contains-duplicate/

from typing import List


class Solution:
    def containsDuplicateSet(self, nums: List[int]) -> bool:
        """
        Set approach

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        seen = set()
        for n in nums:
            if n in seen:
                return True
            seen.add(n)
        return False

    def containsDuplicateSort(self, nums: List[int]) -> bool:
        """
        Sorting approach

        Time complexity:  O(n log n)
        Space complexity: O(1)
        """
        nums.sort()
        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                return True
        return False


# === tests ===

print(Solution().containsDuplicateSet([1, 2, 3, 1]))  # True
print(Solution().containsDuplicateSet([1, 2, 3, 4]))  # False

print(Solution().containsDuplicateSet([1, 2, 3, 1]))  # True
print(Solution().containsDuplicateSet([1, 2, 3, 4]))  # False

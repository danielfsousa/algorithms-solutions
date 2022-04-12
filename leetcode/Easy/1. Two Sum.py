# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Cache numbers in a dictionary to get O(1) access

        Time complexity:  O(n)
        Space complexity: O(n)
        '''
        seen = dict()
        for idx, n in enumerate(nums):
            want = target - n
            if want in seen:
                return [idx, seen[want]]
            seen[n] = idx
        return [-1, -1]


# === tests ===

print(Solution().twoSum([15, 7, 2, 11], target=13))  # (2, 3)

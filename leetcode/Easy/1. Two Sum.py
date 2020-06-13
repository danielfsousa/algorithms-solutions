# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    '''
    Keeps numbers in a dictionary to get O(n) access

    Time complexity:  O(n)
    Space complexity: O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_dict = dict()
        for i in range(len(nums)):
            current_num = nums[i]
            wanted_num = target - current_num
            wanted_num_index = nums_dict.get(wanted_num)
            if wanted_num_index is not None:
                return wanted_num_index, i
            nums_dict[current_num] = i


# === tests ===

print(Solution().twoSum([15, 7, 2, 11], 13))  # (2, 3)

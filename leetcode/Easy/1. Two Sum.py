# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Keeps numbers in a dictionary to get O(n) access

        Time complexity:  O(n)
        Space complexity: O(n)
        '''
        nums_dict = dict()
        for i in range(len(nums)):
            current_num = nums[i]
            wanted_num = target - current_num
            wanted_num_index = nums_dict.get(wanted_num)
            if wanted_num_index is not None:
                return [wanted_num_index, i]
            nums_dict[current_num] = i
        return [-1, -1]


# === tests ===

print(Solution().twoSum([15, 7, 2, 11], target=13))  # (2, 3)

from typing import List


class Solution:
    '''
    Time:  O(n)
    Space: O(n)
    '''
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_hashmap = {}
        for i in range(len(nums)):
            wanted_index = nums_hashmap.get(target - nums[i])
            if wanted_index is not None:
                return wanted_index, i
            nums_hashmap[nums[i]] = i


# === tests ===

print(Solution().twoSum([15, 7, 2, 11], 13))  # (2, 3)

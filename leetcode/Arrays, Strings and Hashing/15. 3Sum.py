from typing import List


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Sort + Two pointers

        Time complexity:  O(n log n) + O(n^2) = O(n^2)
        Space complexity: O(n) - Timsort
        """
        res = []
        nums.sort()

        for i, n in enumerate(nums):
            if i > 0 and nums[i - 1] == n:
                continue

            left, right = i + 1, len(nums) - 1
            while left < right:
                total = n + nums[left] + nums[right]
                if total == 0:
                    res.append([n, nums[left], nums[right]])
                    left += 1
                    while nums[left] == nums[left - 1] and left < right:
                        left += 1
                elif total < 0:
                    left += 1
                else:
                    right -= 1

        return res


# === tests ===

print(Solution().threeSum([-1, 0, 1, 2, -1, -4]))  # [[-1,-1,2], [-1,0,1]]

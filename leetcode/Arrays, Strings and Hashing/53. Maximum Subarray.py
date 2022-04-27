from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        """
        Sliding window like

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        max_subarr = nums[0]
        current_sum = 0
        for n in nums:
            if current_sum < 0:
                current_sum = 0
            current_sum += n
            max_subarr = max(max_subarr, current_sum)
        return max_subarr


# === tests ===

print(Solution().maxSubArray([-2, 1, -3, 4, -1, 2, 1, -5, 4]))  # 6

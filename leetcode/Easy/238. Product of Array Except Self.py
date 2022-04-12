# https://leetcode.com/problems/product-of-array-except-self/

from typing import List


class Solution:
    def productExceptSelfConstantSpace(self, nums: List[int]) -> List[int]:
        """
        Prefix / Postfix precomputation without extra memory

        Time complexity:  O(n)
        Space complexity: O(1) - output list not included
        """
        output = [1] * len(nums)

        prefix = 1
        for i in range(len(nums)):
            output[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in reversed(range(len(nums))):
            output[i] *= postfix
            postfix *= nums[i]

        return output

    def productExceptSelfPrePostfix(self, nums: List[int]) -> List[int]:
        """
        Prefix / Postfix precomputation

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        prefix = [None] * len(nums)
        postfix = [None] * len(nums)
        output = [None] * len(nums)

        for idx, n in enumerate(nums):
            if idx == 0:
                prefix[idx] = n
            else:
                prefix[idx] = n * prefix[idx - 1]

        for idx in reversed(range(len(nums))):
            n = nums[idx]
            if idx == len(nums) - 1:
                postfix[idx] = n
            else:
                postfix[idx] = n * postfix[idx + 1]

        for idx in range(len(nums)):
            preidx = idx - 1
            postidx = idx + 1
            pre = prefix[preidx] if preidx >= 0 else 1
            post = postfix[postidx] if postidx < len(nums) else 1
            output[idx] = pre * post

        return output


# === tests ===

print(Solution().productExceptSelfPrePostfix([1, 2, 3, 4]))  # [24,12,8,6]
print(Solution().productExceptSelfConstantSpace([1, 2, 3, 4]))  # [24,12,8,6]

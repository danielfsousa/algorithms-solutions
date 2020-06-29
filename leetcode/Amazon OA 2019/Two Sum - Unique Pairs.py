# https://leetcode.com/discuss/interview-question/372434

from typing import List


class Solution:
    def twoSumUniquePairs(self, nums: List[int], target: int) -> int:
        """
        Time complexity:  O(n)
        Space complexity: O(n)
        """
        seen = set()
        pairs = set()

        for num in nums:
            wanted = target - num
            if wanted in seen:
                pairs.add(tuple(sorted((num, wanted))))
            else:
                seen.add(num)

        return len(pairs)


# test

print(Solution().twoSumUniquePairs([1, 1, 2, 45, 46, 46], 47)) # 2
print(Solution().twoSumUniquePairs([1, 1], 2)) # 1
print(Solution().twoSumUniquePairs([1, 5, 1, 5], 6)) # 1

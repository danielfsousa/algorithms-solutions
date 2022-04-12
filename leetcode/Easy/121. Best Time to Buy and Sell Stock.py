# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        Sliding window approach

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        left, right = 0, 1
        max_profit = 0
        while right < len(prices):
            is_profitable = prices[left] < prices[right]
            if is_profitable:
                profit = prices[right] - prices[left]
                max_profit = max(max_profit, profit)
            else:
                left = right
            right += 1
        return max_profit


# === tests ===

print(Solution().maxProfit([7, 1, 5, 3, 6, 4]))  # 5

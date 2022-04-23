# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two pointers

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(numbers) - 1
        while left < right:
            res = numbers[left] + numbers[right]
            if res == target:
                return [left + 1, right + 1]
            if res < target:
                left += 1
            else:
                right -= 1
        return []

    def twoSumDictionary(self, numbers: List[int], target: int) -> List[int]:
        """
        Dictionary

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        seen = dict()
        for i, num in enumerate(numbers):
            diff = target - num
            if diff in seen:
                return [seen[diff] + 1, i + 1]
            seen[num] = i

    def twoSumBinarySearch(self, numbers: List[int], target: int) -> List[int]:
        """
        Binary search

        Time complexity:  O(n log n)
        Space complexity: O(1)
        """
        for i in range(len(numbers)):
            left, right = i + 1, len(numbers) - 1
            diff = target - numbers[i]
            while left <= right:
                mid = left + (right - left) // 2
                if numbers[mid] == diff:
                    return [i + 1, mid + 1]
                elif numbers[mid] < diff:
                    left = mid + 1
                else:
                    right = mid - 1

    def twoSumBruteForce(self, numbers: List[int], target: int) -> List[int]:
        """
        Brute Force

        Time complexity:  O(n^2)
        Space complexity: O(1)
        """
        for i in range(len(numbers)):
            for j in range(i + 1, len(numbers)):
                if numbers[i] + numbers[j] == target:
                    return [i + 1, j + 1]


# === tests ===

print(Solution().twoSum([2, 7, 11, 15], 9))  # [1,2]
print(Solution().twoSumDictionary([2, 7, 11, 15], 9))  # [1,2]
print(Solution().twoSumBinarySearch([2, 7, 11, 15], 9))  # [1,2]
print(Solution().twoSumBruteForce([2, 7, 11, 15], 9))  # [1,2]

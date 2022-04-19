# https://leetcode.com/problems/unique-number-of-occurrences/

from typing import List
from collections import Counter


class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        """
        Time complexity:  O(n)
        Space complexity: O(n)
        """
        num_counter = Counter(arr)
        occurencies_set = set(num_counter.values())
        return len(num_counter) == len(occurencies_set)

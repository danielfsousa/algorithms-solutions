# https://leetcode.com/problems/reverse-string/

from typing import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Time complexity:  O(n)
        Space complexity: O(1)
        """
        i = 0
        j = len(s) - 1
        while i < j:
            s[i], s[j] = s[j], s[i]
            i += 1
            j -= 1

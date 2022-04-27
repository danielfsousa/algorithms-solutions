from collections import Counter


class Solution:
    def isAnagramCounter(self, s: str, t: str) -> bool:
        """
        Counter (Dictionary)

        Time complexity:  O(n)
        Space complexity: O(1) - counter has an upper bound of 26 characters
            because s and t consist of lowercase English letters.
        """
        return Counter(s) == Counter(t)

    def isAnagramList(self, s: str, t: str) -> bool:
        """
        List

        Time complexity:  O(n)
        Space complexity: O(1) - count has an upper bound of 26 characters
            because s and t consist of lowercase English letters.
        """
        if len(s) != len(t):
            return False

        def is_zero(num):
            return num == 0

        def charnum(char):
            return ord(char) - ord("a")

        count = [0] * 26

        for char in s:
            count[charnum(char)] += 1

        for char in t:
            count[charnum(char)] -= 1

        return all(map(is_zero, count))

    def isAnagramSorting(self, s: str, t: str) -> bool:
        """
        Sorting

        Time complexity:  O(n log n)
        Space complexity: O(n)
        """
        if len(s) != len(t):
            return False

        sorted_s = sorted(s)
        sorted_t = sorted(t)

        for i in range(len(s)):
            if sorted_s[i] != sorted_t[i]:
                return False

        return True

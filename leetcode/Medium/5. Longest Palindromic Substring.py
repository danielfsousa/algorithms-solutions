class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Expand Around Center

        We observe that a palindrome mirrors around its center.
        Therefore, a palindrome can be expanded from its center, and there are only 2n - 12n−1 such centers.

        Time complexity:  O(n^2)
        Space complexity: O(1)
        """
        start = 0
        end = 0

        for i, _ in enumerate(s):
            odd_length = self.expand_around_center(s, i, i)
            even_length = self.expand_around_center(s, i, i + 1)
            length = max(odd_length, even_length)

            if length > end - start:
                start = i - (length - 1) // 2
                end = i + length // 2

        return s[start:end + 1]

    def expand_around_center(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1
        return right - left - 1

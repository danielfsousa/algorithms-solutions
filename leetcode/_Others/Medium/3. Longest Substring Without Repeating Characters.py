# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window technique

        m = longest substring. In the worst case would be the alphabet size

        Time complexity:  O(n)
        Space complexity: O(m)
        """
        substring_letters = set()
        max_count = 0
        start = 0
        end = 0

        while end < len(s):
            char = s[end]
            if char not in substring_letters:
                substring_letters.add(char)
                end += 1
                max_count = max(max_count, len(substring_letters))
            else:
                substring_letters.remove(s[start])
                start += 1

        return max_count

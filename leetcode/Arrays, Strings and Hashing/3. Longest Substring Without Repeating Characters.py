# https://leetcode.com/problems/longest-substring-without-repeating-characters/


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        Sliding window + hash set

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        seen = set()
        longest_substring = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1
            seen.add(s[right])
            longest_substring = max(longest_substring, right - left + 1)

        return longest_substring

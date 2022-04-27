class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Two pointers without extra space

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        left, right = 0, len(s) - 1

        while left < right:
            if not s[left].isalnum():
                left += 1
                continue
            if not s[right].isalnum():
                right -= 1
                continue
            if s[left].lower() == s[right].lower():
                left += 1
                right -= 1
            else:
                return False

        return True

    def isPalindromeSimpleTwoPointers(self, s: str) -> bool:
        """
        Simple Two pointers

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        filtered_chars = [c.lower() for c in s if c.isalnum()]
        left, right = 0, len(filtered_chars) - 1

        while left < right:
            if filtered_chars[left] != filtered_chars[right]:
                return False
            left += 1
            right -= 1

        return True

class Solution:
    def isValid(self, s: str) -> bool:
        """
        Stack

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        if len(s) % 2 != 0:
            return False

        stack = list()
        mapping = {
            '}': '{',
            ']': '[',
            ')': '('
        }

        for char in s:
            if char in mapping.values():
                stack.append(char)

            elif len(stack) == 0 or stack.pop() != mapping[char]:
                return False

        return len(stack) == 0

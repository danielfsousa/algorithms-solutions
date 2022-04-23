# https://leetcode.com/problems/reverse-linked-list/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Iterative approach

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        prev, current = None, head
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        return prev

    def reverseListRecursive(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """
        Recursive approach

        Time complexity:  O(n)
        Space complexity: O(n)
        """

        def reverse(prev, current):
            if not current:
                return prev
            temp = current.next
            current.next = prev
            return reverse(current, temp)

        return reverse(None, head)


# test
#
# input
#
# 1 -> 2 -> 3 -> 4 -> 5
#
# output
#
# 5 -> 4 -> 3 -> 2 -> 1

head = ListNode()

print(Solution().reverseList(head))

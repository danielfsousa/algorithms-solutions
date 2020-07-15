# https://leetcode.com/problems/reverse-linked-list/submissions/


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        """
        Iterative approach

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        prev = None

        while head:
            head.next, prev, head = prev, head, head.next

        return prev

    def reverseListRecur(self, head: ListNode) -> ListNode:
        """
        Recursive approach

        Time complexity:  O(n)
        Space complexity: O(n)
        """
        if not head or not head.next:
            return head
        n = self.reverseListRecur(head.next)
        head.next.next = head
        head.next = None
        return n

# https://leetcode.com/problems/merge-two-sorted-lists/

from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        """
        Two pointers

        Time complexity:  O(n)
        Space complexity: O(1)
        """
        head = ListNode()
        curr = head

        while list1 and list2:
            if list1.val < list2.val:
                curr.next = list1
                list1 = list1.next
            else:
                curr.next = list2
                list2 = list2.next
            curr = curr.next

        if list1:
            curr.next = list1

        if list2:
            curr.next = list2

        return head.next


# test
#
# input
#
# list1 = 1 -> 2 -> 4
# list2 = 1 -> 3 -> 4
#
# output = 1 -> 1 -> 2 -> 3 -> 4

list1 = ListNode()
list2 = ListNode()

print(Solution().mergeTwoLists(list1, list2))  # 2

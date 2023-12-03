from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(1)
    """
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        left, right = ListNode(), ListNode()

        left_current, right_current = left, right
        while head:
            if head.val < x:
                left_current.next = head
                left_current = left_current.next
            else:
                right_current.next = head
                right_current = right_current.next
            head = head.next

        # key
        right_current.next = None
        left_current.next = right.next
        return left.next

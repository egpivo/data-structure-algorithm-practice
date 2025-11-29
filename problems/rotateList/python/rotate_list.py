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

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k == 0:
            return head

        count = 1
        tail = head
        while tail.next:
            tail = tail.next
            count += 1

        # Key
        tail.next = head
        new_tail = head

        diff = count - (k % count) - 1
        while diff > 0:
            new_tail = new_tail.next
            diff -= 1

        new_head = new_tail.next
        new_tail.next = None
        return new_head

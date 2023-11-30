from typing import Optional



class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution1:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        while head:
            if head.val == 'v':
                return True
            head.val = 'v'
            head = head.next

        return False


class Solution2:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        seen = set()
        while head:
            if head.next in seen:
                return True
            seen.add(head.next)
            head = head.next
        return False


class Solution3:
    """Two pointers"""
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False

        fast_head = head
        slow_head = head

        while fast_head and fast_head.next:
            fast_head = fast_head.next.next
            slow_head = slow_head.next
            if fast_head == slow_head:
                return True
        return False

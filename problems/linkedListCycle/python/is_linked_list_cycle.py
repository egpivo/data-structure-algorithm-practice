from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        # Initialize both pointers at the beginning of the linked list
        slow = fast = head

        while fast and fast.next:
            # Move the slow pointer one step and the fast pointer two steps
            slow = slow.next
            fast = fast.next.next

            # If there's a cycle, the fast pointer will eventually catch up with the slow pointer
            if fast == slow:
                return True

        # If the fast pointer reaches the end of the list, there's no cycle
        return False


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)
    head.next.next.next.next = head.next
    print(f"{Solution().hasCycle(head)}")

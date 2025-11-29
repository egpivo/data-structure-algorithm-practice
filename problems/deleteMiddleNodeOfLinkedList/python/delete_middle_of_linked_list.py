from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """

    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            # If the list is empty or has only one element, nothing to delete
            return None

        slow_pointer = fast_pointer = head
        prev_slow = None

        while fast_pointer and fast_pointer.next:
            # Move slow_pointer one step at a time
            prev_slow = slow_pointer
            slow_pointer = slow_pointer.next
            # Move fast_pointer two steps at a time
            fast_pointer = fast_pointer.next.next

        # Delete the middle node
        if prev_slow:
            prev_slow.next = slow_pointer.next
        else:
            # If prev_slow is None, it means the head is the middle node
            head = head.next

        return head


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)

    middle_node = Solution().deleteMiddle(node)
    while middle_node:
        print(middle_node.val)
        middle_node = middle_node.next

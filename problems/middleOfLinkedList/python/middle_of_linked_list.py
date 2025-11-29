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

    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Initialize fast and slow pointers to the head of the linked list
        fast_pointer = slow_pointer = head

        # Traverse the linked list using the fast and slow pointers
        while fast_pointer and fast_pointer.next:
            # Move the fast pointer two steps at a time
            fast_pointer = fast_pointer.next.next
            # Move the slow pointer one step at a time
            slow_pointer = slow_pointer.next

        # The slow pointer is now at the middle node of the linked list
        return slow_pointer


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)

    middle_node = Solution().middleNode(node)
    while middle_node:
        print(middle_node.val)
        middle_node = middle_node.next

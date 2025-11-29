from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Complexity
    ----------
    - TC:O(n)
    - SC:O(1)
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Reorder the given linked list in-place.

        Args:
            head (ListNode): The head of the linked list.
        """
        if not head or not head.next:
            return

        # Find the middle of the linked list
        slow_pointer = fast_pointer = head
        while fast_pointer and fast_pointer.next:
            fast_pointer = fast_pointer.next.next
            slow_pointer = slow_pointer.next

        # Reverse the second half of the linked list
        reversed_second_half = self.reverseList(slow_pointer.next)
        slow_pointer.next = None  # Break the list into two parts

        # Merge the first and reversed second halves
        current_node = head
        while reversed_second_half:
            next_node = current_node.next
            current_node.next = reversed_second_half
            reversed_second_half = reversed_second_half.next
            current_node.next.next = next_node
            current_node = next_node

    def reverseList(self, head: ListNode) -> ListNode:
        """
        Reverse the given linked list and return the new head.

        Args:
            head (ListNode): The head of the linked list to be reversed.

        Returns:
            ListNode: The head of the reversed linked list.
        """
        previous_node = None
        current_node = head
        while current_node:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        return previous_node


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)

    Solution().reorderList(node)
    while node:
        print(node.val)
        node = node.next

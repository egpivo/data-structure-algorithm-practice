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

    def pairSum(self, head: Optional[ListNode]) -> int:
        # Find the midpoint of the linked list using two pointers
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Reverse the second half of the linked list
        reversed_second_half = self.reverseLinkedList(slow)

        # Find the maximum pair sum of corresponding elements from both halves
        max_pair_sum = float("-inf")
        while head and reversed_second_half:
            max_pair_sum = max(max_pair_sum, head.val + reversed_second_half.val)
            head = head.next
            reversed_second_half = reversed_second_half.next

        return max_pair_sum

    def reverseLinkedList(self, head: ListNode) -> ListNode:
        prev_node = None
        while head:
            next_node = head.next
            head.next = prev_node
            prev_node = head
            head = next_node
        return prev_node


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(2)
    node.next.next.next = ListNode(1)

    print(f"{Solution().pairSum(node)}")

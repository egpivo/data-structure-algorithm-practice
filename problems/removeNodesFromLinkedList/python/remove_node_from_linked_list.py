# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution1:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        stack = [dummy]

        current = head
        while current:
            # Only pop when the current value is greater than the stack's top value
            while len(stack) > 1 and stack[-1].val < current.val:
                stack.pop()
            # Link the last node in the stack to the current node
            stack[-1].next = current
            stack.append(current)
            current = current.next

        return dummy.next


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def removeNodes(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Base case: if head is None or head.next is None, return head
        if not head or not head.next:
            return head

        # Recursively call removeNodes to process the rest of the linked list
        head.next = self.removeNodes(head.next)

        # If the current node's value is less than the next node's value,
        # return the next node (effectively removing the current node)
        if head.val < head.next.val:
            return head.next

        # Otherwise, return the current node
        return head


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(1)
    head.next.next.next = ListNode(4)
    current = head
    print("Input")
    while current:
        print(current.val)
        current = current.next

    result = Solution1().removeNodes(head)
    print("Output1")
    current = result
    while current:
        print(current.val)
        current = current.next

    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)
    current = head
    print("Input")
    while current:
        print(current.val)
        current = current.next

    result = Solution2().removeNodes(head)
    print("Output2")
    current = result
    while current:
        print(current.val)
        current = current.next

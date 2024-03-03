# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Complexity
    ----------
    - TC: O(N)
    - SC: O(1)
    """

    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if head.next == None:
            return None
        tmp = head

        for i in range(n):
            tmp = tmp.next
        if tmp == None:
            return head.next
        else:
            keep = head
            while tmp.next != None:
                keep = keep.next
                tmp = tmp.next

            keep.next = keep.next.next
            return head


class Solution2:
    """
    Complexity
    ----------
    - TC: O(N)
    - SC: O(1)
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        if not head or n <= 0:
            return head

        length = 0
        current_node = head

        # Count the length of the linked list
        while current_node:
            current_node = current_node.next
            length += 1

        # Reset current_node to the head for traversal
        current_node = head
        steps_to_remove = length - n

        # Handle the case where the first node needs to be removed
        if steps_to_remove == 0:
            return head.next

        # Traverse to the node before the one to be removed
        for _ in range(steps_to_remove - 1):
            current_node = current_node.next

        # Remove the nth node from the end
        current_node.next = current_node.next.next

        return head


class Solution3:
    """
    - Notes: two-pointer

    Complexity
    ----------
    - TC: O(N)
    - SC: O(1)
    """

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        while n > 0:
            fast = fast.next
            n -= 1

        if not fast:
            return head.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
        return head


if __name__ == "__main__":
    data = ListNode(1)
    data.next = ListNode(2)
    data.next.next = ListNode(3)
    data.next.next.next = ListNode(4)
    data.next.next.next.next = ListNode(5)

    ans = Solution()

    ansList = ans.removeNthFromEnd(data, 2)
    for i in range(4):
        print("%d \t" % ansList.val)
        ansList = ansList.next

    data = ListNode(1)
    data.next = ListNode(2)
    data.next.next = ListNode(3)
    data.next.next.next = ListNode(4)
    data.next.next.next.next = ListNode(5)

    ans = Solution2()

    ansList = ans.removeNthFromEnd(data, 2)
    for i in range(4):
        print("%d \t" % ansList.val)
        ansList = ansList.next

    data = ListNode(1)
    data.next = ListNode(2)
    data.next.next = ListNode(3)
    data.next.next.next = ListNode(4)
    data.next.next.next.next = ListNode(5)

    ans = Solution3()

    ansList = ans.removeNthFromEnd(data, 2)
    for i in range(4):
        print("%d \t" % ansList.val)
        ansList = ansList.next

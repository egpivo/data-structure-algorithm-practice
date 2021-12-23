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
        fast = slow = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        return slow


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)

    middle_node = Solution().middleNode(node)
    while middle_node:
        print(middle_node.val)
        middle_node = middle_node.next

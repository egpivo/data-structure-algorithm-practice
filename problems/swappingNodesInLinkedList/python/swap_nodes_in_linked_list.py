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

    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        # Initialize pointers for the kth and (n-k)th nodes
        kth_node = nth_k_node = head

        # Traverse to the kth node
        for _ in range(k - 1):
            kth_node = kth_node.next

        # Mark the kth node and start traversing
        swap_node = kth_node
        kth_node = kth_node.next

        # Traverse until the kth node reaches the end
        while kth_node:
            kth_node = kth_node.next
            nth_k_node = nth_k_node.next

        # Swap values of the kth and (n-k)th nodes
        swap_node.val, nth_k_node.val = nth_k_node.val, swap_node.val

        return head


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(3)
    node.next.next.next = ListNode(4)

    middle_node = Solution().swapNodes(node, 2)
    while middle_node:
        print(middle_node.val)
        middle_node = middle_node.next

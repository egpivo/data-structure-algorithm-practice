# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Complexity
    ----------
    - TC: O(1)
    - SC: O(1)
    """

    def deleteNode(self, node):
        """
        :type node: ListNode
        :rtype: void Do not return anything, modify node in-place instead.
        """
        # Copy the value of the next node to the current node
        node.val = node.next.val

        # Remove the next node by updating the pointers
        node.next = node.next.next


if __name__ == "__main__":
    head = ListNode(3)
    head.next = ListNode(2)
    head.next.next = ListNode(0)
    head.next.next.next = ListNode(4)
    current = head
    print("Input")
    while current:
        print(current.val)
        current = current.next

    node = head.next.next
    print(f"Node: {node.val}")
    Solution().deleteNode(node)
    print("Output")
    current = head
    while current:
        print(current.val)
        current = current.next

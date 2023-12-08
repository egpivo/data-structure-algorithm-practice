# Definition for a Node.
class Node:
    def __init__(self, x: int, next: "Node" = None, random: "Node" = None):
        self.val = int(x)
        self.next = next
        self.random = random


class Solution:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """

    def copyRandomList(self, head: "Optional[Node]") -> "Optional[Node]":
        if not head:
            return None

        head_dict = {}
        current = head

        while current:
            head_dict[current] = Node(current.val)
            current = current.next

        current = head
        while current:
            head_dict[current].next = head_dict.get(current.next)
            head_dict[current].random = head_dict.get(current.random)
            current = current.next

        return head_dict[head]

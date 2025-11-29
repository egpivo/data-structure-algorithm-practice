import math
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Complexity
    ----------
    - TC: O(nm)
    - SC: O(1)
    """

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        current = head

        while current and current.next:
            prev = current
            current = current.next

            gcd = self.calculate_greatest_common_divisor(prev.val, current.val)
            prev.next = ListNode(gcd)
            prev.next.next = current
        return head

    def calculate_greatest_common_divisor(self, num1, num2):
        if num1 < num2:
            num1, num2, = (
                num2,
                num1,
            )

        gcd = num2
        while gcd > 0:
            if num1 % gcd == 0 and num2 % gcd == 0:
                return gcd
            gcd -= 1
        return gcd


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n\log m)
    - SC: O(1)
    """

    def insertGreatestCommonDivisors(
        self, head: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not head or not head.next:
            return (
                head  # If the list is empty or has only one node, return it unchanged
            )

        prev = head
        while prev.next:
            current = prev.next
            gcd = math.gcd(prev.val, current.val)
            new_node = ListNode(gcd)
            new_node.next = current
            prev.next = new_node
            prev = current  # Move prev to the next pair of nodes

        return head


if __name__ == "__main__":
    head = ListNode(18)
    head.next = ListNode(6)
    head.next.next = ListNode(10)
    head.next.next.next = ListNode(3)
    ans1 = Solution().insertGreatestCommonDivisors(head)
    while ans1:
        print(ans1.val)
        ans1 = ans1.next

    print("Second answer")
    head = ListNode(18)
    head.next = ListNode(6)
    head.next.next = ListNode(10)
    head.next.next.next = ListNode(3)

    ans2 = Solution2().insertGreatestCommonDivisors(head)

    while ans2:
        print(ans2.val)
        ans2 = ans2.next

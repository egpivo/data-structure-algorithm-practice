# Definition for singly-linked list.
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
    - SC: O(n)
    """

    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        dummy.next = head
        prefix_sum = 0
        prefix_sum_map = {0: dummy}

        current = head

        while current:
            prefix_sum += current.val

            if prefix_sum in prefix_sum_map:
                prev = prefix_sum_map[prefix_sum].next
                temp = prefix_sum + prev.val

                while temp != prefix_sum:
                    del prefix_sum_map[temp]
                    prev = prev.next
                    temp += prev.val

                prefix_sum_map[prefix_sum].next = current.next
            else:
                prefix_sum_map[prefix_sum] = current

            current = current.next

        return dummy.next


if __name__ == "__main__":
    array = ListNode(1)
    head = array
    for num in [2, 3, -3, 4]:
        head.next = ListNode(num)
        head = head.next
    result = Solution().removeZeroSumSublists(array)
    while result:
        print(result.val)
        result = result.next

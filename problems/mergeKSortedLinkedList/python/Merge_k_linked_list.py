from heapq import heappop, heappush
from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = None


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(n\cdot k)$
    - Space complexity: $O(1)$
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        result = lists[0]
        for node in lists[1:]:
            result = self.merge(result, node)

        return result

    def merge(
        self, first: Optional[ListNode], second: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        while first and second:
            if first.val < second.val:
                current.next, first = first, first.next
            else:
                current.next, second = second, second.next
            current = current.next

        current.next = first if first else second
        return dummy.next


class Solution2:
    """
    Complexity
    ----------
    - Time complexity: $O(n\log k)$
    - Space complexity: $O(k)$
    """

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None
        k = len(lists)
        result = ListNode(None)
        current = result

        priority_queue = []
        for index in range(k):
            if lists[index]:
                heappush(priority_queue, (lists[index].val, index))
                lists[index] = lists[index].next

        while priority_queue:
            value, index = heappop(priority_queue)
            current.next = ListNode(value)
            current = current.next
            if lists[index]:
                heappush(priority_queue, (lists[index].val, index))
                lists[index] = lists[index].next

        return result.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(4)
    l1.next.next = ListNode(5)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l3 = ListNode(2)
    l3.next = ListNode(6)
    lists = [l1, l2, l3]

    ans = Solution()
    newlist = ans.mergeKLists(lists)

    for i in range(8):
        print("%d \t" % newlist.val)
        newlist = newlist.next

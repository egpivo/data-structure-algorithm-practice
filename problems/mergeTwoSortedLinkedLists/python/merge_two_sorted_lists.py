# Definition for singly-linked list.
from typing import Optional
import copy


class ListNode:
    def __init__(self, x=0, next=None):
        self.val = x
        self.next = next


class Solution:
    """
    Comlextity
    ----------
    - n: # of nodes in list1
    - m : # of nodes in list2
    - TC: O(n + m)
    - SC: O (n + m)
    """

    def mergeTwoLists(
            self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if not l1 and not l2:
            return None
        if l1 is None:
            return l2
        if l2 is None:
            return l1

        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


class SolutionIterative:
    """
    Comlextity
    ----------
    - n: # of nodes in list1
    - m : # of nodes in list2
    - TC: O(n + m)
    - SC: O (n + m)
    """

    def mergeTwoLists(
            self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        prev = prehead = ListNode(-1)
        while l1 and l2:
            if l1.val < l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next
        prev.next = l1 if l1 is not None else l2
        return prehead.next


if __name__ == "__main__":
    l1 = ListNode(1)
    l1.next = ListNode(2)
    l1.next.next = ListNode(4)

    l2 = ListNode(1)
    l2.next = ListNode(3)
    l2.next.next = ListNode(4)

    l11 = copy.deepcopy(l1)
    l22 = copy.deepcopy(l2)
    ans = Solution()
    new_list = ans.mergeTwoLists(l1, l2)
    for i in range(6):
        print("Recursive: %d \t" % new_list.val)
        new_list = new_list.next

    new_list_iterative = SolutionIterative().mergeTwoLists(l11, l22)
    for i in range(6):
        print("Iterative: %d \t" % new_list_iterative.val)
        new_list_iterative = new_list_iterative.next

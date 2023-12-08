from typing import List, Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists:
            return None

        val_list = []
        for node in lists:
            while node:
                val_list.append(node.val)
                node = node.next
        head = ListNode(None)
        forward = head

        for val in val_list:
            forward.next = ListNode(val)
            forward = forward.next
        return head.next


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

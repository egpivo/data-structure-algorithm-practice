# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        init = ListNode(-1)
        init.next = head

        current = head
        previous = init
        while current:
            while current.next and current.next.val == current.val:
                current = current.next

            if previous.next == current:
                previous = previous.next
                current = current.next
            else:
                previous.next = current.next
                current = previous.next

        return init.next


if __name__ == "__main__":
    data = ListNode(1)
    data.next = ListNode(2)
    data.next.next = ListNode(2)
    data.next.next.next = ListNode(4)
    data.next.next.next.next = ListNode(5)

    ans = Solution()

    answer_list = ans.deleteDuplicates(data)
    while answer_list:
        print("%d \t" % answer_list.val)
        answer_list = answer_list.next

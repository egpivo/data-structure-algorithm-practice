from typing import Optional


# Definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        """brute force"""
        if head is None:
            return None

        all_values = []
        while head:
            all_values.append(head.val)
            head = head.next

        all_values.sort()
        answer = ListNode()
        forward = answer

        for value in all_values:
            forward.next = ListNode(value)
            forward = forward.next

        return answer.next


class SolutionMergeSort:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return head

        fast, slow = head.next, head
        while fast and fast.next:
            fast, slow = fast.next.next, slow.next

        mid, slow.next = slow.next, None

        first_half = self.sortList(head)
        second_half = self.sortList(mid)

        merged_list = self.merge(first_half, second_half)
        return merged_list

    def merge(self, first: ListNode, second: ListNode) -> ListNode:
        dummy = ListNode()
        current = dummy

        while first and second:
            if first.val < second.val:
                current.next, first = first, first.next
            else:
                current.next, second = second, second.next
            current = current.next

        if first:
            current.next = first
        if second:
            current.next = second

        return dummy.next


def convert_to_list(head: ListNode) -> list:
    output = []
    while head:
        output.append(head.val)
        head = head.next
    return output


def convert_to_linked_list(input: list) -> ListNode:
    if len(input) == 0:
        return None

    head = ListNode(input[0])
    if len(input) > 1:
        input = input[1:]
        head.next = convert_to_linked_list(input)
    return head


if __name__ == "__main__":
    input = [1, 2, 5, 3, 6, 4]
    reversed = Solution().sortList(convert_to_linked_list(input))
    print(convert_to_list(reversed))

    input = [1, 2, 5, 3, 6, 4]
    reversed = SolutionMergeSort().sortList(convert_to_linked_list(input))
    print(convert_to_list(reversed))

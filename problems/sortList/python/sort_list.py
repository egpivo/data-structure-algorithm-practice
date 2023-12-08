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

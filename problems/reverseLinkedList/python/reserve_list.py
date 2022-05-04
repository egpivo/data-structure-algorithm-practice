from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


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


class Solution:
    """
    Note
    ----
    - Time complexity: O(N)
    - Space complexity: O(1)
    """

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None:
            return None

        forward = None
        while head:
            prev, head.next = head.next, forward
            forward, head = head, prev

        return forward


if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6]
    reverse_list = Solution().reverseList
    output = convert_to_list(reverse_list(convert_to_linked_list(input)))
    print(output)
    assert output == [6, 5, 4, 3, 2, 1], "wrong answer"

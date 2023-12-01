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
    def reverseBetween(
        self, head: Optional[ListNode], left: int, right: int
    ) -> Optional[ListNode]:
        if head is None:
            return None

        previous = None
        current = head
        while left > 1:
            previous = current
            current = current.next
            left -= 1
            right -= 1

        tail, con = current, previous

        # previous will contain the reverse list
        while right > 0 and current is not None:
            temp = current.next
            current.next = previous
            previous = current
            current = temp
            right -= 1

        if con is not None:
            con.next = previous
        else:
            # if left is the starting point
            head = previous
        # if right != length of the list
        tail.next = current
        return head


if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6]
    reverse_list = Solution().reverseBetween
    output = convert_to_list(reverse_list(convert_to_linked_list(input), 3, 5))
    print(output)
    assert output == [1, 2, 5, 4, 3, 6], "wrong answer"

    output = convert_to_list(reverse_list(convert_to_linked_list(input), 1, 5))
    print(output)
    assert output == [5, 4, 3, 2, 1, 6], "wrong answer"

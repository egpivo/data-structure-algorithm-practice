# Definition for singly-linked list.
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
    Example
    -------
    >>> input = [1, 2, 3, 4, 5]
    >>> head = convert_to_linked_list(input)
    >>> output = convert_to_list(Solution().reverseList(head))
    >>> print(output)
    [5, 4, 3, 2, 1]
    
    """

    def reverseList(self, head: ListNode) -> ListNode:
        if head is None:
            return head

        foward = ListNode(None)

        while head is not None:
            temp = head.next
            head.next = None if foward.val is None else foward
            foward = head
            head = temp

        head = foward
        return head


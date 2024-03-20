# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    """
    Complexity
    ----------
    - TC: O(m + n)
    - SC: O(1)
    """

    def mergeInBetween(
        self, list1: ListNode, a: int, b: int, list2: ListNode
    ) -> ListNode:
        # Initialize pointers for the first and second stop nodes
        first_stop = second_stop = list1

        # Move the first_stop pointer to the node before the sublist to be replaced
        for _ in range(a - 1):
            first_stop = first_stop.next
            second_stop = second_stop.next

        # Move the second_stop pointer to the last node of the sublist to be replaced
        for _ in range(b - a + 1):
            second_stop = second_stop.next

        # Find the last node of list2
        list2_last = list2
        while list2_last.next:
            list2_last = list2_last.next

        # Connect the sublist before first_stop to list2 and list2 to the sublist after second_stop
        first_stop.next, list2_last.next = list2, second_stop.next

        return list1


if __name__ == "__main__":
    head1 = ListNode(10)
    head1.next = ListNode(1)
    head1.next.next = ListNode(13)
    head1.next.next.next = ListNode(6)
    head1.next.next.next.next = ListNode(9)
    head1.next.next.next.next.next = ListNode(5)

    head2 = ListNode(1000000)
    head2.next = ListNode(1000001)
    head2.next.next = ListNode(1000002)

    answer = Solution().mergeInBetween(head1, 3, 4, head2)
    while answer:
        print(answer.val)
        answer = answer.next

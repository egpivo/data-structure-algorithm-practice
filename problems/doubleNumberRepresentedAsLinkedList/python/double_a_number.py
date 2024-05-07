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
    Complexity
    ----
    - Time complexity: O(N)
    - Space complexity: O(1)
    """

    def doubleIt(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Reverse the linked list
        reversed_list = self.reverse(head)

        current = reversed_list
        remaining = 0

        while current:
            # Double the value of the current node and add the remaining value
            current.val *= 2
            current.val += remaining
            # Update the remaining value for the next node
            remaining = current.val // 10
            current.val %= 10
            # Move to the next node
            if current.next:
                current = current.next
            else:
                break

        # If there's a remaining value after the last node, append a new node
        if remaining:
            current.next = ListNode(remaining)

        # Reverse the modified list and return
        return self.reverse(reversed_list)

    # Function to reverse a linked list
    def reverse(self, node):
        reversed_list = None
        current = node

        while current:
            temp, current.next = current.next, reversed_list
            reversed_list, current = current, temp
        return reversed_list


if __name__ == "__main__":
    input = [1, 2, 3, 4, 5, 6]
    head = convert_to_linked_list(input)
    result = Solution().doubleIt(head)
    output = convert_to_list(result)
    print(output)

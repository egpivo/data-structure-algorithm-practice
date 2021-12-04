from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class SolutionBruteForce:
    """

    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []
        current_node = head
        while current_node:
            vals.append(current_node.val)
            current_node = current_node.next
        return vals == vals[::-1]


class SolutionRescursive:
    """

    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        self.front_pointer = head

        def recursively_check(current_node):
            if current_node is not None:
                if not recursively_check(current_node.next):
                    return False

                if self.front_pointer.val != current_node.val:
                    return False
                self.front_pointer = self.front_pointer.next
            return True

        return recursively_check(head)


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        if head is None:
            return True
        temp_head = head
        first_half_end = self.find_the_first_half_end(temp_head)
        reserved_second_half = self.reverse_linked_list(first_half_end.next)

        while temp_head and reserved_second_half:
            if temp_head.val != reserved_second_half.val:
                return False
            else:
                temp_head = temp_head.next
                reserved_second_half = reserved_second_half.next

        return True

    def find_the_first_half_end(self, node: ListNode) -> ListNode:
        fast = slow = node
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        return slow

    def reverse_linked_list(self, node: ListNode) -> ListNode:
        current = node
        head = None

        while current:
            temp = current.next
            current.next = head
            head = current
            current = temp

        return head


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(2)
    node.next.next = ListNode(2)
    node.next.next.next = ListNode(1)

    print(f"{SolutionBruteForce().isPalindrome(node)}")
    print(f"{SolutionRescursive().isPalindrome(node)}")
    print(f"{Solution().isPalindrome(node)}")

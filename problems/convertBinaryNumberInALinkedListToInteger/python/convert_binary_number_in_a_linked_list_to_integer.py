# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        """
        Complexity
        ---------
        - TC: O(n)
        - SC: O(1)
        """
        answer = 0
        while head:
            answer = answer * 2 + head.val
            head = head.next

        return answer


if __name__ == "__main__":
    node = ListNode(1)
    node.next = ListNode(0)
    node.next.next = ListNode(1)

    print(f"{Solution().getDecimalValue(node)}")

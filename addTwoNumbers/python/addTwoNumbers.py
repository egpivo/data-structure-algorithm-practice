# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode

        Complextity
        -----------
        - m: the length of l1
        - n: the lenght of l2

        TC: O(max(m + n))
        SC: O(max(m + n))
        """
        ls = ListNode(0)
        temp = ls
        rest = 0

        while l1 or l2 or rest:
            sum = (l1.val if l1 else 0) + (l2.val if l2 else 0) + rest
            rest = sum // 10
            temp.next = ListNode(sum % 10)
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            temp = temp.next

        return ls.next


if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))

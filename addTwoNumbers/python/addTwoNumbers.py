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
      """
      ls = ListNode(0)
      temp = ls
      rest = 0

      while(l1 != None or  l2 != None or rest):
        sum = (l1.val if l1!= None else 0) + (l2.val if l2 != None else 0) + rest
        rest = 1 if sum >= 10 else 0
        temp.next = ListNode(sum%10)
        l1 = l1.next if l1!= None else None
        l2 = l2.next if l1!= None else None
        temp = temp.next

      return ls.next

if __name__ == '__main__':
    a, a.next, a.next.next = ListNode(2), ListNode(4), ListNode(3)
    b, b.next, b.next.next = ListNode(5), ListNode(6), ListNode(4)
    result = Solution().addTwoNumbers(a, b)
    print("{0} -> {1} -> {2}".format(result.val, result.next.val, result.next.next.val))

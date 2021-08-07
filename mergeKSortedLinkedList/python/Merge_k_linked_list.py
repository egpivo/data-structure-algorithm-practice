# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists: return None

        # first step: store val in a new list
        res = []
        for l in lists:
            while l != None:
                res.append(l.val)
                l = l.next
        # second: sorting
        res.sort()

        # third: pass vals back to a linked list
        head = ListNode(None)
        p = head
        for i in res:
            p.next = ListNode(i)
            p = p.next
        return head.next


if __name__=="__main__":
  l1 = ListNode(1)
  l1.next = ListNode(4)
  l1.next.next = ListNode(5)

  l2 = ListNode(1)
  l2.next = ListNode(3)
  l2.next.next = ListNode(4)

  l3 = ListNode(2)
  l3.next = ListNode(6)
  lists = [l1, l2, l3]

  ans = Solution()
  newlist = ans.mergeKLists(lists)

  for i in range(8):
    print("%d \t" % newlist.val)
    newlist = newlist.next

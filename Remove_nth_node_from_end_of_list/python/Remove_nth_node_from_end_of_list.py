# Definition for singly-linked list.
class ListNode:
  def __init__(self, x):
       self.val = x
       self.next = None

class Solution:
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        if(head.next == None):
            return None
        tmp = head;

        for i in range(n):
            tmp = tmp.next
        if(tmp == None):
            return head.next
        else:
            keep = head
            while(tmp.next != None):
                keep = keep.next
                tmp = tmp.next

            keep.next = keep.next.next
            return head

if __name__ == "__main__":
  data = ListNode(1)
  data.next = ListNode(2)
  data.next.next = ListNode(3)
  data.next.next.next = ListNode(4)
  data.next.next.next.next = ListNode(5)

  ans = Solution()

  ansList = ans.removeNthFromEnd(data, 2)
  for i in range(4):
    print("%d \t"% ansList.val)
    ansList = ansList.next

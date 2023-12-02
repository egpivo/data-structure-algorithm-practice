# Definition for singly-linked list.
from typing import Optional


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



class Solution2:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        total = 0

        current = head
        while current:
            current = current.next
            total += 1
        if total == n:
            return head.next

        previous = None
        current = head
        position = total - n + 1

        while position > 1:
            previous = current
            current = current.next
            position -= 1

        if current and current.next:
            previous.next = previous.next.next
        else:
            previous.next = None
        return head


class Solution3:
    """
    - Notes: two-pointer
    """
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        fast = head
        slow = head

        while n > 0:
            fast = fast.next
            n -= 1

        if not fast:
            return head.next

        while fast and fast.next:
            fast = fast.next
            slow = slow.next

        slow.next = slow.next.next
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


  data = ListNode(1)
  data.next = ListNode(2)
  data.next.next = ListNode(3)
  data.next.next.next = ListNode(4)
  data.next.next.next.next = ListNode(5)

  ans = Solution2()

  ansList = ans.removeNthFromEnd(data, 2)
  for i in range(4):
    print("%d \t"% ansList.val)
    ansList = ansList.next


  data = ListNode(1)
  data.next = ListNode(2)
  data.next.next = ListNode(3)
  data.next.next.next = ListNode(4)
  data.next.next.next.next = ListNode(5)

  ans = Solution3()

  ansList = ans.removeNthFromEnd(data, 2)
  for i in range(4):
    print("%d \t"% ansList.val)
    ansList = ansList.next

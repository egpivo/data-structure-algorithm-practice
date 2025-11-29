# Definition for singly-linked list.
from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionPreorder:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def preorder(left):
            if not left:
                return

            prev, mid = self.find_mid_node(left)

            right = mid.next
            prev.next = None

            node = TreeNode(val=mid.val)
            if left != mid:
                node.left = preorder(left)
            node.right = preorder(right)
            return node

        return preorder(head)

    def find_mid_node(self, current: Optional[ListNode]) -> Optional[ListNode]:
        fast = current
        slow = current
        prev = slow
        while fast.next and fast.next.next:
            prev = slow
            fast = fast.next.next
            slow = slow.next
        return prev, slow


class SolutionInorder:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def inorder(start, end):
            nonlocal head
            if start > end:
                return
            mid = start + (end - start) // 2
            left = inorder(start, mid - 1)

            node = TreeNode(val=head.val)
            node.left = left
            head = head.next
            node.right = inorder(mid + 1, end)
            return node

        current, length = head, 0
        while current:
            current = current.next
            length += 1
        return inorder(0, length - 1)


def inorder(tree):
    if tree != None:
        inorder(tree.left)
        print(tree.val)
        inorder(tree.right)


def preorder(tree):
    if tree != None:
        print(tree.val)
        preorder(tree.left)
        preorder(tree.right)


def postorder(tree):
    if tree != None:
        postorder(tree.left)
        postorder(tree.right)
        print(tree.val)


if __name__ == "__main__":
    l1 = ListNode(-10)
    l1.next = ListNode(-3)
    l1.next.next = ListNode(0)
    l1.next.next.next = ListNode(5)
    l1.next.next.next.next = ListNode(9)

    ans = SolutionInorder()
    ansTree = ans.sortedListToBST(l1)

    print("Preorder\n")
    preorder(ansTree)
    print("Inorder\n")
    inorder(ansTree)
    print("Postorder\n")
    postorder(ansTree)

    ans = SolutionPreorder()
    ansTree = ans.sortedListToBST(l1)

    print("Preorder\n")
    preorder(ansTree)
    print("Inorder\n")
    inorder(ansTree)
    print("Postorder\n")
    postorder(ansTree)

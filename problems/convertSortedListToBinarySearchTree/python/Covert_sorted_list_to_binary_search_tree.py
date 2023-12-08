# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """
        if head == None:
            return None

        first = head
        second = head
        third = second

        while (first.next != None) and (first.next.next != None):
            third = second
            second = second.next
            first = first.next.next

        first = second.next
        third.next = None

        ans = TreeNode(second.val)

        if head != second:
            ans.left = self.sortedListToBST(head)
        ans.right = self.sortedListToBST(first)

        return ans


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

    ans = Solution()
    ansTree = ans.sortedListToBST(l1)

    print("Preorder\n")
    preorder(ansTree)
    print("Inorder\n")
    inorder(ansTree)
    print("Postorder\n")
    postorder(ansTree)

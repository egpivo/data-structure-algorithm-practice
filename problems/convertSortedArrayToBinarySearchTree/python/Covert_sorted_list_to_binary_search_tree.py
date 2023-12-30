# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def preorder(nums_slice: List[int]) -> TreeNode:
            if not nums_slice:
                return None
            mid = len(nums_slice) // 2
            root = TreeNode(nums_slice[mid])
            root.left = self.sortedArrayToBST(nums_slice[:mid])
            root.right = self.sortedArrayToBST(nums_slice[mid + 1 :])
            return root

        return preorder(nums)


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
    nums = [-10, -3, 0, 5, 9]

    ans = Solution()
    ansTree = ans.sortedArrayToBST(nums)

    print("Preorder\n")
    preorder(ansTree)
    print("Inorder\n")
    inorder(ansTree)
    print("Postorder\n")
    postorder(ansTree)

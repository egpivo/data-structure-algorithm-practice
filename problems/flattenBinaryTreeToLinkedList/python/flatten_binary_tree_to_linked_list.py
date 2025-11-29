import copy
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        if root is None:
            return None

        # preorder traversal
        stack_bag = [root]
        values = []
        while stack_bag:
            head = stack_bag.pop()
            values.append(head.val)

            if head.right is not None:
                stack_bag.append(head.right)
            if head.left is not None:
                stack_bag.append(head.left)

        # to linked list
        pointer = root
        for value in values[1:]:
            pointer.right = TreeNode(value)
            pointer.left = None
            pointer = pointer.right


class Solution2:
    def flattenTree(self, node):
        if node is None:
            return None

        if node.left is None and node.right is None:
            return node

        left_tail = self.flattenTree(node.left)
        right_tail = self.flattenTree(node.right)

        if left_tail:
            left_tail.right = node.right
            node.right = node.left
            node.left = None

        return right_tail if right_tail else left_tail

    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        self.flattenTree(root)


def show(node: TreeNode) -> None:
    if node is None:
        return None
    print(f"{node.val}")
    show(node.left)
    show(node.right)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(1000)
    tree.left.left = TreeNode(2000)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)

    tree2 = copy.deepcopy(tree)
    ans = Solution()
    ans.flatten(tree)
    print(f"After flattening,")
    show(tree)

    ans = Solution2()
    ans.flatten(tree)
    print(f"[2nd solution]After flattening,")
    show(tree)

from typing import Optional, List

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

    ans = Solution()
    ans.flatten(tree)
    print(f"After flattening,")
    show(tree)


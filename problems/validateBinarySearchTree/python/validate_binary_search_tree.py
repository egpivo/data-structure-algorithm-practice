from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(H)
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True

            if lower < node.val < upper:
                return dfs(node.left, lower, node.val) and dfs(
                    node.right, node.val, upper
                )
            else:
                return False

        return dfs(root, -float("inf"), float("inf"))


class SolutionRecursive:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(H)
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        previous = -float("inf")
        result = True

        def inorder(node):
            nonlocal previous, result
            if not node or not result:
                return

            inorder(node.left)
            if previous >= node.val:
                result = False
                return

            previous = node.val
            inorder(node.right)

        inorder(root)
        return result


class SolutionIterative:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        previous = -float("inf")
        stack = deque()

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if previous >= root.val:
                return False
            previous = root.val
            root = root.right
        return True


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(2)
    print(f"The answer is {Solution().isValidBST(tree)}")
    print(f"The answer is {SolutionRecursive().isValidBST(tree)}")
    print(f"The answer is {SolutionIterative().isValidBST(tree)}")

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
    Notes
    -----
    - H: tree height
    - Time complexity: O(N)
    - Space complexity: O(H)
    """

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = float("inf")
        previous = None

        def inorder(node):
            nonlocal result, previous
            if not node:
                return
            inorder(node.left)
            if previous is not None:
                result = min(result, node.val - previous)
            previous = node.val
            inorder(node.right)

        inorder(root)
        return result


class Solution2:
    """
    Notes
    -----
    - H: tree height
    - Time complexity: O(N)
    - Space complexity: O(H)
    """

    def getMinimumDifference(self, root: Optional[TreeNode]) -> int:
        result = float("inf")
        previous = None
        stack = deque([])

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            if previous is not None and result > root.val - previous:
                result = root.val - previous

            previous = root.val
            root = root.right
        return result


if __name__ == "__main__":
    bst = TreeNode(4)
    bst.left = TreeNode(2)
    bst.right = TreeNode(6)
    bst.left.left = TreeNode(1)
    bst.left.right = TreeNode(3)

    print(f"The answer is {Solution().getMinimumDifference(bst)}")
    print(f"The answer is {Solution2().getMinimumDifference(bst)}")

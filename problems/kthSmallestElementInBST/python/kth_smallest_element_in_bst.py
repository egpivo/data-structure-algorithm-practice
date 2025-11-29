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

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        def inorder(node):
            nonlocal k
            if not node:
                return
            left_result = inorder(node.left)
            if left_result is not None:
                return left_result
            k -= 1
            if k == 0:
                return node.val
            return inorder(node.right)

        return inorder(root)


class Solution2:
    """
    Notes
    -----
    - H: tree height
    - Time complexity: O(N)
    - Space complexity: O(H)
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        stack = deque()

        while stack or root:
            while root:
                stack.append(root)
                root = root.left

            root = stack.pop()
            k -= 1

            if k == 0:
                return root.val

            root = root.right


if __name__ == "__main__":
    bst = TreeNode(4)
    bst.left = TreeNode(2)
    bst.right = TreeNode(6)
    bst.left.left = TreeNode(1)
    bst.left.right = TreeNode(3)

    print(f"The answer is {Solution().kthSmallest(bst, 2)}")
    print(f"The answer is {Solution2().kthSmallest(bst, 2)}")

# Definition for singly-linked list.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Complexity
    ----------
    - TC: O(n + m)
    - SC: O(n + m)
    """

    def mergeTrees(
        self, root1: Optional[TreeNode], root2: Optional[TreeNode]
    ) -> Optional[TreeNode]:
        if not root1:
            return root2
        if not root2:
            return root1

        return self.dfs(root1, root2)

    def dfs(self, root1, root2):
        if root1.val and root2.val:
            root1.val += root2.val

        if root1.left and root2.left:
            self.dfs(root1.left, root2.left)
        elif root2.left:
            root1.left = root2.left

        if root1.right and root2.right:
            self.dfs(root1.right, root2.right)
        elif root2.right:
            root1.right = root2.right

        return root1

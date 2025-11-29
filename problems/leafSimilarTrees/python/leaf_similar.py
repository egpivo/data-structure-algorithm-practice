# Definition for a binary tree node.
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $ O(N_1 + N_2)$
    - Space complexity: $O(\max(H_1, H_2))$
    """

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        leaves1 = self.collect_leaves(root1)
        leaves2 = self.collect_leaves(root2)
        return leaves1 == leaves2

    def collect_leaves(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        leaves = []
        stack = [root]

        while stack:
            current_node = stack.pop()

            if not current_node.left and not current_node.right:
                leaves.append(current_node.val)

            if current_node.right:
                stack.append(current_node.right)
            if current_node.left:
                stack.append(current_node.left)

        return leaves

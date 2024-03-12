# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(h)
    """

    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def check_balance(node):
            if not node:
                return 0

            left_height = check_balance(node.left) + 1 if node.left else 0
            right_height = check_balance(node.right) + 1 if node.right else 0

            if abs(left_height - right_height) > 1:
                return float("-inf")  # Unbalanced subtree indicator

            return max(left_height, right_height)

        return check_balance(root) != float("-inf")


if __name__ == "__main__":
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)
    root.right.right = TreeNode(val=4)
    root.right.right.right = TreeNode(val=5)
    root.right.right.right.left = TreeNode(val=16)
    root.right.right.right.right = TreeNode(val=6)
    print(f"{Solution().isBalanced(root)}")

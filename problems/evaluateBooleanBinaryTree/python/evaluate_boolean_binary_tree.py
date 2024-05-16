# Definition for a binary tree node.
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
    - TC: O(n)
    - SC: O(h)
    """

    def evaluateTree(self, root: Optional[TreeNode]) -> Optional[int]:
        def evaluate(node):
            # Base case: if the node is None or a leaf, return its value
            if not node or not (node.left or node.right):
                return node.val if node else None

            # Recursively evaluate left and right subtrees
            left_val = evaluate(node.left)
            right_val = evaluate(node.right)

            # Update the value of the current node based on its type
            if left_val is not None and right_val is not None:
                node.val = (
                    max(left_val, right_val)
                    if node.val == 2
                    else min(left_val, right_val)
                )

            return node.val if node else None

        return evaluate(root)


if __name__ == "__main__":
    root = TreeNode(val=2)
    root.left = TreeNode(val=1)
    root.right = TreeNode(val=3)
    root.right.left = TreeNode(val=0)
    root.right.right = TreeNode(val=1)

    print(f"{Solution().evaluateTree(root)}")

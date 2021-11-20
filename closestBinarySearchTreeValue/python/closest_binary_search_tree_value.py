from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Algorithm
        ---------
        1. Build an inorder traversal array.
        2. Find the closest to target element in that array.

        Complexity
        ----------
        TC: O(N)
        SC: O(N) (inorder traversal)
        """
        def inorder(node):
            return inorder(node.left) + [node.val] + inorder(node.right) if node else []

        return min(inorder(root), key=lambda x: abs(target - x))


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right = TreeNode(5)
    target = 3.714286
    print(f"The answer is {Solution().closestValue(tree, target)}")

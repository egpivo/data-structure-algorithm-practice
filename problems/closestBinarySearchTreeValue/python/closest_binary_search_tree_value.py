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


class OpimizedSolution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        """
        Complexity
        ----------
        - k: an index of closest element
        - H: height
        TC:
          - avg O(k) (balance tree)
          - worst case O(H + k)
        SC: O(H)
        """
        stack = []
        min_val = float("-inf")

        while stack or root:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()

            if min_val <= target <= root.val:
                return min(min_val, root.val, key=lambda x: abs(target - x))

            min_val = root.val
            root = root.right

        return min_val


if __name__ == "__main__":
    tree = TreeNode(4)
    tree.left = TreeNode(2)
    tree.left.left = TreeNode(1)
    tree.left.right = TreeNode(3)
    tree.right = TreeNode(5)
    target = 3.714286
    print(f"The answer is {Solution().closestValue(tree, target)}")
    print(f"The optimized answer is {OpimizedSolution().closestValue(tree, target)}")

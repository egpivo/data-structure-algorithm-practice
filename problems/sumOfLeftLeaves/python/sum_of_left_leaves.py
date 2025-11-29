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
    - TC: O(N)
    - SC: O(H)
    """

    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0

        def dfs(node):
            nonlocal total
            if not node:
                return
            if node.left and not node.left.left and not node.left.right:
                total += node.left.val
            dfs(node.left)
            dfs(node.right)

        dfs(root)
        return total


if __name__ == "__main__":
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print(f"The solution is {Solution().sumOfLeftLeaves(root)}")

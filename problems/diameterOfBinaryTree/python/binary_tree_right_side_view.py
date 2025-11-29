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
    - SC: O(h)
    """

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(node):
            nonlocal result
            if not node:
                return 0

            left_depth = dfs(node.left)
            right_depth = dfs(node.right)
            result = max(result, left_depth + right_depth)

            return 1 + max(left_depth, right_depth)

        dfs(root)
        return result


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(5)

    print(f"The DFS answer is {Solution().diameterOfBinaryTree(tree)}")

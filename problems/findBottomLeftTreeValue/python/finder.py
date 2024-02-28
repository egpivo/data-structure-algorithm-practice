from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Note
    ----
    - H: tree height
    - Time complexity: O(N)
    - Space complexity: O(H)
    """

    def findBottomLeftValue(self, root: Optional[TreeNode]) -> int:
        max_level, last_left = -1, None

        def dfs(node, level):
            nonlocal max_level, last_left

            if not node:
                return None, 0

            left_most, left_level = dfs(node.left, level + 1)
            right_most, right_level = dfs(node.right, level + 1)

            if not left_most and not right_most and level > max_level:
                last_left, max_level = node.val, level

            return left_most or right_most, max(left_level, right_level)

        dfs(root, 0)
        return last_left


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(5)

    print(f"The DFS answer is {Solution().findBottomLeftValue(tree)}")

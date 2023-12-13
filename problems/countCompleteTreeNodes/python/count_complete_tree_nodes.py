from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """Not valid solution for the criteria
    Note
    ----
    - H: tree height
    - Time complexity: O(N)
    - Space complexity: O(H)
    """

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        def dfs(node, total):
            if not node:
                return 0
            if node.left:
                total = dfs(node.left, total + 1)
            if node.right:
                total = dfs(node.right, total + 1)
            return total

        return dfs(root, 1)


class Solution2:
    """Not valid solution for the criteria
    Note
    ----
    - H: tree height
    - Time complexity: O(log N * log N)
    - Space complexity: O(H)
    """

    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        left_depth = self.get_depth(root, direction="left")
        right_depth = self.get_depth(root, direction="right")

        if left_depth == right_depth:
            return 2 ** (left_depth + 1) - 1
        else:
            return self.countNodes(root.left) + self.countNodes(root.right) + 1

    def get_depth(self, node: Optional[TreeNode], direction: str) -> int:
        total = 0
        while (direction == "left" and node.left) or (
            direction == "right" and node.right
        ):
            total += 1
            node = node.left if direction == "left" else node.right
        return total


if __name__ == "__main__":
    complete_tree = TreeNode(1)
    complete_tree.left = TreeNode(2)
    complete_tree.right = TreeNode(3)
    complete_tree.left.left = TreeNode(4)

    print(f"The answer is {Solution().countNodes(complete_tree)}")
    print(f"The answer is {Solution2().countNodes(complete_tree)}")

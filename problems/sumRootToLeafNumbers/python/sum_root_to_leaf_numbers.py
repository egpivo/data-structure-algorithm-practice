from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionDFS:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        if not root:
            return None
        if not root.left and not root.right:
            return root.val

        def dfs(node, total):
            if not node:
                return 0
            if not node.left and not node.right:
                return node.val + 10 * total
            return dfs(node.left, node.val + 10 * total) + dfs(
                node.right, node.val + 10 * total
            )

        return dfs(root, 0)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    print(SolutionDFS().sumNumbers(tree))

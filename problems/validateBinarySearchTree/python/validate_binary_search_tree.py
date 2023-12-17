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
    - SC: O(H)
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def dfs(node, lower, upper):
            if not node:
                return True

            if lower < node.val < upper:
                return dfs(node.left, lower, node.val) and dfs(
                    node.right, node.val, upper
                )
            else:
                return False

        return dfs(root, -float("inf"), float("inf"))


class SolutionRecursive:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(H)
    """

    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        previous = -float("inf")
        result = True

        def inorder(node):
            nonlocal previous, result
            if not node:
                return

            inorder(node.left)
            if previous >= node.val:
                result = False
                return

            previous = node.val
            inorder(node.right)

        inorder(root)
        return result


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(2)
    print(f"The answer is {Solution().isValidBST(tree)}")
    print(f"The answer is {SolutionRecursive().isValidBST(tree)}")

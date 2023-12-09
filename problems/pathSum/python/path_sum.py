from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    """
    Notes
    ----
    - TC: O(N)
    - SC: O(H)
    """

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False

        def dfs(node, count):
            if not node:
                if count == targetSum:
                    return True
            elif not node.right and not node.left:
                count += node.val
                if count == targetSum:
                    return True
            count += node.val
            if node.left:
                if dfs(node.left, count):
                    return True
            if node.right:
                if dfs(node.right, count):
                    return True
            return False

        return dfs(root, 0)


class SolutionBFS:
    """
    Notes
    ----
    - TC: O(N)
    - SC: O(H)
    """

    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        queue = [(root, root.val)]
        while queue:
            node, value = queue.pop(0)
            if not node.left and not node.right:
                if value == targetSum:
                    return True
            else:
                if node.left:
                    queue.append((node.left, value + node.left.val))
                if node.right:
                    queue.append((node.right, value + node.right.val))
        return False


if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(8)
    tree.right = TreeNode(11)
    tree.right.left = TreeNode(3)

    print(Solution().hasPathSum(tree, 17))
    print(SolutionBFS().hasPathSum(tree, 17))

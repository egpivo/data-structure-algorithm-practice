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


if __name__ == "__main__":
    tree = TreeNode(5)
    tree.left = TreeNode(4)
    tree.left.left = TreeNode(8)
    tree.right = TreeNode(11)
    tree.right.left = TreeNode(3)

    ans = Solution()
    print(ans.hasPathSum(tree, 17))

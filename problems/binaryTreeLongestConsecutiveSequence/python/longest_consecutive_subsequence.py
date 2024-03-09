# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# dfs
class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def longestConsecutive(self, root: TreeNode) -> int:
        def dfs(node):
            if not node:
                return 0
            left_count = right_count = 1
            if node.left:
                left_count = (
                    dfs(node.left) + 1
                    if node.left.val == node.val + 1
                    else dfs(node.left)
                )
            if node.right:
                right_count = (
                    dfs(node.right) + 1
                    if node.right.val == node.val + 1
                    else dfs(node.right)
                )
            return max(left_count, right_count)

        return dfs(root)


if __name__ == "__main__":
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)
    root.right.right = TreeNode(val=4)
    root.right.right.right = TreeNode(val=5)
    root.right.right.right.left = TreeNode(val=16)
    root.right.right.right.right = TreeNode(val=6)
    print(f"{Solution().longestConsecutive(root)}")

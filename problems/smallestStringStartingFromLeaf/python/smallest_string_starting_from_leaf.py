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

    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        min_path = chr(
            ord("z") + 1
        )  # Initialize with a path that's guaranteed to be greater

        def dfs(node, path):
            nonlocal min_path

            if not node:
                return
            path += chr(ord("a") + node.val)
            if not node.left and not node.right:
                # If it's a leaf node, compare the path with the current minimum
                min_path = min(min_path, path[::-1])
            else:
                dfs(node.left, path)
                dfs(node.right, path)

        dfs(root, "")
        return min_path


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(2)
    tree.right = TreeNode(3)

    print(Solution().smallestFromLeaf(tree))

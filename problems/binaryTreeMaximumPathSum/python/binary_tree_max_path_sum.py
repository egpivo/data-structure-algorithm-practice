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
    - Time complexity: O(N)
    - Space complexity: O(H)
    """

    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        max_sum = -float("inf")

        def path_sum(node):
            nonlocal max_sum
            if not node:
                return 0

            left_path_sum = max(0, path_sum(node.left))
            right_path_sum = max(0, path_sum(node.right))
            max_sum = max(max_sum, node.val + left_path_sum + right_path_sum)

            return node.val + max(left_path_sum, right_path_sum, 0)

        _ = path_sum(root)
        return max_sum


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    ans = Solution()
    print(f"The answer is {ans.maxPathSum(tree)}")

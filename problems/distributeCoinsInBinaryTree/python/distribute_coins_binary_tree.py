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

    def distributeCoins(self, root: Optional[TreeNode]) -> int:
        steps = 0

        def dfs(node):
            nonlocal steps
            if not node:
                return 0

            left_excess = dfs(node.left)
            right_excess = dfs(node.right)

            # Total steps is the sum of absolute values of excess coins moved from left and right children
            steps += abs(left_excess) + abs(right_excess)

            # Return the number of excess coins for the current node
            # -1 accounts for leaving one coin for the current node
            return node.val + left_excess + right_excess - 1

        dfs(root)
        return steps


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.right = TreeNode(0)
    tree.right.left = TreeNode(0)
    ans = Solution()
    print(f"The answer is {ans.distributeCoins(tree)}")

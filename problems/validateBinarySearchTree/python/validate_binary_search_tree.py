from typing import Optional, List

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
    - SC: O(n)
    """
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def dfs(node, lower, upper):
            if not node:
                return True

            if lower < node.val < upper:
                return (
                    dfs(node.left, lower, node.val)
                    and dfs(node.right, node.val, upper)
                )
            else:
                return False
        return dfs(root, -float('inf'), float('inf'))


class SolutionRecursive:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self.inorderTraversal(root.left) + [root.val] + self.inorderTraversal(root.right) if root else []

if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(3)
    tree.right.left = TreeNode(2)
    ans = Solution()
    print(f"The answer is {ans.isValidBST(tree)}")


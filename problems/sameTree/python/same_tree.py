from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Solution:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if not q and not p:
            return True
        elif (p and not q) or (q and not p) or p.val != q.val:
            return False

        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    tree2 = TreeNode(3)
    tree2.left = TreeNode(9)
    tree2.right = TreeNode(20)
    tree2.right.left = TreeNode(15)
    tree2.right.right = TreeNode(7)

    ans = Solution()
    print(ans.isSameTree(tree, tree2))

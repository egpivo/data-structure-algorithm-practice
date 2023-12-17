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
    -----
    - H: tree height
    - Time complexity: O(N)
    - Space complexity: O(H)
    """

    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        collections = []

        def inorder(node):
            if not node:
                return
            inorder(node.left)
            if len(collections) == k:
                return
            collections.append(node.val)
            inorder(node.right)

        inorder(root)
        return collections[-1]


if __name__ == "__main__":
    bst = TreeNode(4)
    bst.left = TreeNode(2)
    bst.right = TreeNode(6)
    bst.left.left = TreeNode(1)
    bst.left.right = TreeNode(3)

    print(f"The answer is {Solution().kthSmallest(bst, 2)}")

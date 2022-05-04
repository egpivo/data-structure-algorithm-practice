from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if self.isMatched(root, subRoot): return True
        if not root: return False
        return (
            self.isSubtree(root.left, subRoot) or 
            self.isSubtree(root.right, subRoot)
        )    

    def isMatched(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not (root and subRoot):
            return root is subRoot

        return (
            root.val == subRoot.val and
            self.isMatched(root.left, subRoot.left) and
            self.isMatched(root.right, subRoot.right)
        )

if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.right = TreeNode(7)

    subTree = TreeNode(20)
    subTree.left = TreeNode(15)
    subTree.right = TreeNode(7)

    print(Solution().isSubtree(tree, subTree))
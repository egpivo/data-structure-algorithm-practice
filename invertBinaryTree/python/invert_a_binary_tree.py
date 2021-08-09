from copy import deepcopy
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        copied_root_left = deepcopy(root.left)
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(copied_root_left)

        return root


def show(node: TreeNode) -> None:
    if node is None:
        return None
    print(f"{node.val}")
    show(node.left)
    show(node.right)


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.right = TreeNode(2)
    ans = Solution()
    show(ans.invertTree(tree))

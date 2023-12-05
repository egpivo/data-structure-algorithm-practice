from copy import deepcopy
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
    - TC: O(n)
    - SC: O(n)
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        copied_root_left = deepcopy(root.left)
        root.left = self.invertTree(root.right)
        root.right = self.invertTree(copied_root_left)

        return root


class SolutionBFS:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        queue = [root]
        while queue:
            level = len(queue)

            for _ in range(level):
                node = queue.pop(-1)
                if node.right:
                    queue.append(node.right)
                if node.left:
                    queue.append(node.left)
                node.left, node.right = node.right, node.left
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

    tree = TreeNode(1)
    tree.left = TreeNode(3)
    tree.right = TreeNode(2)
    ans = SolutionBFS()
    show(ans.invertTree(tree))

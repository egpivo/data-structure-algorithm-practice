# Definition for a binary tree node.
from collections import deque
from typing import Optional


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

    def addOneRow(
        self, root: Optional[TreeNode], val: int, depth: int
    ) -> Optional[TreeNode]:
        if depth == 1:
            return TreeNode(val, left=root)

        queue = deque([root])
        level = 1

        while queue and level < depth - 1:
            level += 1
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        # Insert new nodes at the specified depth
        for node in queue:
            node.left, node.right = TreeNode(val, left=node.left), TreeNode(
                val, right=node.right
            )

        return root


def show(node: TreeNode) -> None:
    if node is None:
        return None
    print(f"{node.val}")
    show(node.left)
    show(node.right)


if __name__ == "__main__":
    root = TreeNode(val=1)
    root.left = TreeNode(val=2)
    root.right = TreeNode(val=3)
    root.right.right = TreeNode(val=4)
    root.right.right.right = TreeNode(val=5)
    root.right.right.right.left = TreeNode(val=16)
    root.right.right.right.right = TreeNode(val=6)
    print("original tree")
    show(root)

    result = Solution().addOneRow(root, depth=2, val=100)

    print("modified tree")
    show(result)

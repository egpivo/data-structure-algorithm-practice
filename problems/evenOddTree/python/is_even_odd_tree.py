from collections import deque
from sys import maxsize
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
    - TC: O(n)
    - SC: O(n)
    """

    def isEvenOddTree(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True  # An empty tree is considered an even-odd tree

        queue = deque([root])
        level = 0

        while queue:
            size = len(queue)
            prev_val = -maxsize if level % 2 == 0 else maxsize

            for _ in range(size):
                node = queue.popleft()

                if (level % 2 == 0 and (prev_val >= node.val or node.val % 2 == 0)) or (
                    level % 2 == 1 and (prev_val <= node.val or node.val % 2 == 1)
                ):
                    return False

                prev_val = node.val

                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

            level += 1

        return True


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(5)

    print(f"The BFS answer is {Solution().isEvenOddTree(tree)}")

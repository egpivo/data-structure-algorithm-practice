from collections import deque
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
    - The key poiont to solving the problem is to set a index to each node

    Complextiy
    ----------
    - D: tree diameter
    - Time complexity: O(N)
    - Space complexity: O(D)
    """

    def isCompleteTree(self, root: Optional[TreeNode]) -> bool:
        q = deque([(root, 1)])
        expected_num = 1

        while q:
            level = len(q)
            for _ in range(level):
                node, idx = q.popleft()
                if idx != expected_num:
                    return False
                expected_num += 1

                if node.left:
                    q.append((node.left, idx * 2))
                if node.right:
                    q.append((node.right, idx * 2 + 1))

        return True


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(4)

    print(f"The BFS answer is {Solution().isCompleteTree(tree)}")

    tree2 = TreeNode(1)
    tree2.left = TreeNode(2)
    tree2.right = TreeNode(3)
    tree2.left.left = TreeNode(4)
    tree2.left.right = TreeNode(5)
    tree2.right.left = TreeNode(6)

    print(f"The BFS answer is {Solution().isCompleteTree(tree2)}")

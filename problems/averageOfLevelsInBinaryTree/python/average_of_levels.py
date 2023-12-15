from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class BFSSolution:
    """
    Note
    ----
    - D: tree diameter
    - Time complexity: O(N)
    - Space complexity: O(D)
    """

    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        answer = []

        if not root:
            return answer

        queue = deque([root])

        while queue:
            level = len(queue)
            count = 0
            for _ in range(level):
                node = queue.popleft()
                count += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            answer.append(count / level)
        return answer


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(5)

    print(f"The BFS answer is {BFSSolution().averageOfLevels(tree)}")

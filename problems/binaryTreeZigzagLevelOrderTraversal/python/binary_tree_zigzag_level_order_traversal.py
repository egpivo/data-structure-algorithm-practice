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

    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        answer = []
        if not root:
            return answer

        queue = deque([root])
        level = 0
        while queue:
            size = len(queue)
            collector = []
            level += 1
            for _ in range(size):
                node = queue.popleft()
                collector.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if level % 2 == 1:
                answer.append(collector)
            else:
                collector.reverse()
                answer.append(collector)
        return answer


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(5)

    print(f"The BFS answer is {BFSSolution().zigzagLevelOrder(tree)}")

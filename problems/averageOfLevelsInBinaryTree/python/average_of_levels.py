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
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_sum = sum(node.val for node in queue)
            result.append(level_sum / level_size)

            for _ in range(level_size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result


class DFSSolution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        def dfs(node, level, level_sums, level_counts):
            if not node:
                return

            if level < len(level_sums):
                level_sums[level] += node.val
                level_counts[level] += 1
            else:
                level_sums.append(node.val)
                level_counts.append(1)

            dfs(node.left, level + 1, level_sums, level_counts)
            dfs(node.right, level + 1, level_sums, level_counts)

        level_sums, level_counts = [], []
        dfs(root, 0, level_sums, level_counts)

        return [
            level_sum / level_count
            for level_sum, level_count in zip(level_sums, level_counts)
        ]


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(5)

    print(f"The BFS answer is {BFSSolution().averageOfLevels(tree)}")
    print(f"The DFS answer is {DFSSolution().averageOfLevels(tree)}")

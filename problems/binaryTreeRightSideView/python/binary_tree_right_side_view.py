from collections import deque
from typing import List, Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class DFSSolution:
    """
    Note
    ----
    - H: tree height
    - Time complexity: O(N)
    - Space complexity: O(H)
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        result = []
        if not root:
            return result

        self.dfs(root, 0, result)
        return result

    def dfs(self, node, depth, result):
        if depth == len(result):
            result.append(node.val)

        if node.right:
            self.dfs(node.right, depth + 1, result)
        if node.left:
            self.dfs(node.left, depth + 1, result)


class BFSSolution:
    """
    Note
    ----
    - D: tree diameter
    - Time complexity: O(N)
    - Space complexity: O(D)
    """

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        answer = []
        if root is None:
            return answer
        q = deque([root])

        answer = []
        while q:
            level_length = len(q)

            for i in range(level_length):
                node = q.popleft()
                if i == level_length - 1:
                    answer.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return answer


if __name__ == "__main__":
    tree = TreeNode(1)
    tree.right = TreeNode(2)
    tree.right.left = TreeNode(3)
    tree.right.right = TreeNode(5)

    print(f"The DFS answer is {DFSSolution().rightSideView(tree)}")
    print(f"The BFS answer is {BFSSolution().rightSideView(tree)}")

from collections import deque
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionIterative:
    """
    Note
    ----
    - N: # nodes
    - TC: O(N)
    - SC: O(N)
    """

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        answer = 0
        stack = [root]
        while stack:
            node = stack.pop()
            if node:
                if low <= node.val <= high:
                    answer += node.val
                if low < node.val:
                    stack.append(node.left)
                if high > node.val:
                    stack.append(node.right)
        return answer


class SolutionDFSRecursive:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        self.answer = 0

        def dfs(node):
            if node:
                if low <= node.val <= high:
                    self.answer += node.val
                if low < node.val:
                    dfs(node.left)
                if high > node.val:
                    dfs(node.right)

        dfs(root)
        return self.answer


class SolutionDFSRecursive2:
    """This is thread-safe version"""

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0
        else:
            total = 0
            if low <= root.val <= high:
                total += root.val
            if low < root.val:
                total += self.rangeSumBST(root.left, low, high)
            if high > root.val:
                total += self.rangeSumBST(root.right, low, high)
        return total


class SolutionBFS:
    """
    Note
    ----
    - N: # nodes
    - TC: O(N)
    - SC: O(N)
    """

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        answer = 0
        q = deque([root])

        while q:
            level = len(q)
            for _ in range(level):
                node = q.popleft()
                if node:
                    if low <= node.val <= high:
                        answer += node.val
                    if node.val > low:
                        q.append(node.left)
                    if node.val < high:
                        q.append(node.right)
        return answer


if __name__ == "__main__":
    root = TreeNode(10)
    root.left = TreeNode(5)
    root.right = TreeNode(15)
    root.left.left = TreeNode(3)
    root.left.right = TreeNode(7)
    root.right.right = TreeNode(18)
    low = 7
    high = 15
    print(SolutionIterative().rangeSumBST(root, low, high))
    print(SolutionDFSRecursive().rangeSumBST(root, low, high))
    print(SolutionDFSRecursive2().rangeSumBST(root, low, high))
    print(SolutionBFS().rangeSumBST(root, low, high))

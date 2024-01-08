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
    - SC: O(H)
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
    - SC: O(H)
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


class SolutionTest:
    """
    - binary tree
        - left < right
        - level i root > level i+1 root

    - data structure: use an integer variable
    - algorithm:
        - recursively sum up the node in the range until the invalid node occurs

    """

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if root is None:
            return 0

        result = 0

        def recursive(node):
            nonlocal result

            if low <= node.val <= high:
                result += node.val
            if node.left and node.val > low:
                recursive(node.left)
            if node.right and node.val < high:
                recursive(node.right)

        recursive(root)
        return result


class SolutionSimpleDFS:
    """
    Note
    ----
    - N: # nodes
    - TC: O(N)
    - SC: O(H)
    """

    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        if not root:
            return 0
        result = root.val if low <= root.val <= high else 0
        return (
            result
            + self.rangeSumBST(root.left, low, high)
            + self.rangeSumBST(root.right, low, high)
        )


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
    print(SolutionTest().rangeSumBST(root, low, high))
    print(SolutionSimpleDFS().rangeSumBST(root, low, high))

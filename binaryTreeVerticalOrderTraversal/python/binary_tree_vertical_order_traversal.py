from typing import Optional, List
from collections import defaultdict, deque


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class SolutionBFS:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Complexity
        ---------
        - N = # of nodes
        - TC: O(NlogN) (due to the sort with the worst case)
        - SC: O(N)
        """
        if root is None:
            return []
        column_table = defaultdict(list)
        # collect (node, column position)
        queue = deque([(root, 0)])

        while queue:
            node, column = queue.popleft()

            if node is not None:
                column_table[column].append(node.val)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [column_table[x] for x in sorted(column_table.keys())]


class SolutionBFSWithoutSorting:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Complexity
        ---------
        - p = # of nodes
        - TC: O(p)
        - SC: O(p)
        """
        if root is None:
            return []

        column_table = defaultdict(list)
        # collect (node, column position)
        queue = deque([(root, 0)])
        min_column = max_column = 0
        while queue:
            node, column = queue.popleft()

            if node is not None:
                column_table[column].append(node.val)
                min_column = min(min_column, column)
                max_column = max(max_column, column)
                queue.append((node.left, column - 1))
                queue.append((node.right, column + 1))

        return [column_table[x] for x in range(min_column, max_column + 1)]


class SolutionDFS:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        """
        Complexity
        ---------
        - W = width of the tree
        - H = height of the tree
        - p = # nodes of the tree
        - TC: O(W⋅HlogH)
        - SC: O(p)
        """
        if root is None:
            return []

        column_table = defaultdict(list)
        # collect (node, column position)
        min_column = max_column = 0

        def dfs(node, row, column):
            nonlocal min_column, max_column
            if node is not None:
                column_table[column].append((row, node.val))
                min_column = min(min_column, column)
                max_column = max(max_column, column)

                dfs(node.left, row + 1, column - 1)
                dfs(node.right, row + 1, column + 1)

        dfs(root, 0, 0)
        result = []
        for column in range(min_column, max_column + 1):
            # sort by row
            column_table[column].sort(key=lambda x: x[0])
            column_vals = [val for _, val in column_table[column]]
            result.append(column_vals)
        return result


if __name__ == "__main__":
    tree = TreeNode(3)
    tree.left = TreeNode(9)
    tree.right = TreeNode(20)
    tree.right.left = TreeNode(15)
    tree.right.left = TreeNode(7)
    print(f"The answer is {SolutionBFS().verticalOrder(tree)}")
    print(f"The answer is {SolutionBFSWithoutSorting().verticalOrder(tree)}")
    print(f"The answer is {SolutionDFS().verticalOrder(tree)}")

from typing import List


class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(n)$
        - $n$ is the total number of elements in the grid, as we visit each element once.
    - Space complexity: $O(n)$
        -  due to the recursive calls, with the maximum depth of recursion proportional to the size of the grid.
    """

    def construct(self, grid: List[List[int]]) -> "Node":
        if not grid:
            return None
        placeholder = 0

        def helper(row: int, col: int, size: int) -> Node:
            if size == 1:
                return Node(grid[row][col] == 1, True)

            half_size = size // 2
            top_left = helper(row, col, half_size)
            top_right = helper(row, col + half_size, half_size)
            bottom_left = helper(row + half_size, col, half_size)
            bottom_right = helper(row + half_size, col + half_size, half_size)

            if all(
                child.isLeaf and child.val == top_left.val
                for child in [top_right, bottom_left, bottom_right]
            ):
                return Node(top_left.val, True)

            return Node(
                placeholder, False, top_left, top_right, bottom_left, bottom_right
            )

        return helper(0, 0, len(grid))

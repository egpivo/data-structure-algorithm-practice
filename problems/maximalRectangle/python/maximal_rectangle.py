from collections import deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(m * n)
    - SC: O(n)
    """

    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix:
            return 0

        m, n = len(matrix), len(matrix[0])
        max_area = 0
        # Adding sentinel to the heights array to force the stack to pop out entirely
        heights = [0] * (n + 1)

        for row in range(m):
            for col in range(n):
                if matrix[row][col] == "1":
                    heights[col] += 1
                else:
                    heights[col] = 0

            max_area = max(max_area, self.compute_max_area(heights))

        return max_area

    def compute_max_area(self, heights: List[int]) -> int:
        stack = deque()
        max_area = 0

        for col, h in enumerate(heights):
            while stack and h < heights[stack[-1]]:
                height = heights[stack.pop()]
                width = col if not stack else col - stack[-1] - 1
                max_area = max(max_area, height * width)

            stack.append(col)

        return max_area


if __name__ == "__main__":
    matrix = [
        ["1", "0", "1", "0", "0"],
        ["1", "0", "1", "1", "1"],
        ["1", "1", "1", "1", "1"],
        ["1", "0", "0", "1", "0"],
    ]
    print(f"The solution is {Solution().maximalRectangle(matrix)}")

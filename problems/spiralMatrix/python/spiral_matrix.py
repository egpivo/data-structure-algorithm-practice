from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(nrows * ncols)
    - SC: O(1) (don't include the output array in the space complexity)
    """

    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        nrows = len(matrix)
        ncols = len(matrix[0])

        left, up = 0, 0
        right, down = ncols - 1, nrows - 1

        answer = []

        while len(answer) < nrows * ncols:
            for col in range(left, right + 1):
                answer.append(matrix[up][col])

            for row in range(up + 1, down + 1):
                answer.append(matrix[row][right])

            if up != down:
                for col in range(right - 1, left - 1, -1):
                    answer.append(matrix[down][col])
            if left != right:
                for row in range(down - 1, up, -1):
                    answer.append(matrix[row][left])

            left += 1
            right -= 1
            up += 1
            down -= 1

        return answer


if __name__ == "__main__":
    matrix = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
    print(f"{Solution().spiralOrder(matrix)}")

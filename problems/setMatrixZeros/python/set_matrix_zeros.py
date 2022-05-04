from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(MN)
    - SC: O(M + N)
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        nrows = len(matrix)
        ncols = len(matrix[0])

        zero_row_indices = set()
        zero_col_indices = set()

        for i in range(nrows):
            for j in range(ncols):
                if matrix[i][j] == 0:
                    zero_row_indices.add(i)
                    zero_col_indices.add(j)

        for i in zero_row_indices:
            matrix[i][:] = [0] * ncols

        for j in zero_col_indices:
            for i in range(nrows):
                matrix[i][j] = 0


class Solution2:
    """
    Complexity
    ----------
    - TC: O(MN)
    - SC: O(1)
    """

    def setZeroes(self, matrix: List[List[int]]) -> None:
        nrows = len(matrix)
        ncols = len(matrix[0])
        is_first_col_zero = False
        is_first_row_zero = False

        for i in range(nrows):
            if matrix[i][0] == 0:
                is_first_col_zero = True
                break
        for j in range(ncols):
            if matrix[0][j] == 0:
                is_first_row_zero = True
                break

        for i in range(1, nrows):
            for j in range(1, ncols):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, nrows):
            for j in range(1, ncols):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if is_first_col_zero:
            for i in range(nrows):
                matrix[i][0] = 0

        if is_first_row_zero:
            matrix[0][:] = [0] * ncols


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    print(f"Solution is {matrix}")

    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution2().setZeroes(matrix)
    print(f"Solution is {matrix}")
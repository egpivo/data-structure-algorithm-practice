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


if __name__ == "__main__":
    matrix = [[1, 1, 1], [1, 0, 1], [1, 1, 1]]
    Solution().setZeroes(matrix)
    print(f"Solution is {matrix}")

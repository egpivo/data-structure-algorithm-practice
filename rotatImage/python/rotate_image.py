from typing import List


class Solution:
    """
    Compexlity
    ----------
    - TCL O(N^2)
    - SC: O(1)
    """
    def rotate(self, matrix: List[List[int]]) -> None:
        self.transpose(matrix)
        self.relect(matrix)

    def transpose(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix[0])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    def relect(self, matrix: List[List[int]]) -> None:
        for i in range(len(matrix)):
            for j in range(len(matrix[0]) // 2):
                matrix[i][j], matrix[i][len(matrix[0]) - j - 1] = matrix[i][len(matrix[0]) - j - 1], matrix[i][j]


if __name__ == "__main__":
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
Solution().rotate(matrix)
print(f"Solution: {matrix}")

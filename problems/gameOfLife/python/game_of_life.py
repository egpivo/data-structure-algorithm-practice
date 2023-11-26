from typing import List


class Solution(object):
    """
    Complexity
    ----------
    - TC: O(MN)
    - SC: O(MN)
    """

    def gameOfLife(self, board: List[List[int]]) -> None:
        nrows = len(matrix)
        ncols = len(matrix[0])
        state = [[False] * ncols for _ in range(nrows)]

        for i in range(nrows):
            for j in range(ncols):
                state[i][j] = self.does_change(board, i,j)

        for i in range(nrows):
            for j in range(ncols):
                if state[i][j]:
                    board[i][j] = 0 if board[i][j] else 1

    def does_change(self, board: List[List[int]], i: int, j: int) -> bool:
        nrows = len(matrix)
        ncols = len(matrix[0])

        lives = sum(
            board[i + i_shift][j + j_shift]
            for i_shift in range(-1, 2)
            for j_shift in range(-1, 2)
            if 0 <= i + i_shift < nrows and 0 <= j + j_shift < ncols and not (i_shift == 0 and j_shift == 0)
        )
        if board[i][j]:
            if not(2 <= lives <= 3):
                return True
        else:
            if lives == 3:
                return True
        return False


if __name__ == "__main__":
    matrix = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Solution().gameOfLife(matrix)
    print(f"Solution is {matrix}")

    matrix = [[1,1],[1,0]]
    Solution().gameOfLife(matrix)
    print(f"Solution is {matrix}")

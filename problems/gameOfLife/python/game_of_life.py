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

class Solution2(object):
    """
    Complexity
    ----------
    - TC: O(MN)
    - SC: O(1)
    """
    def gameOfLife(self, board: List[List[int]]) -> None:
        directions = [(i, j) for i in range(-1, 2) for j in range(-1, 2) if not (i == 0 and j == 0)]

        m = len(board)
        n = len(board[0])
        live_tag = 2
        death_tag = -1

        for row in range(m):
            for col in range(n):
                lives = sum(
                    abs(board[row+ix][col+iy]) == 1
                    for ix, iy in directions
                    if 0 <= row+ix < m and 0 <= col+iy <n
                )
                if board[row][col] == 1 and not lives in (2, 3):
                    board[row][col] = death_tag
                elif board[row][col] == 0 and lives == 3:
                    board[row][col] = live_tag

        for row in range(m):
            for col in range(n):
                board[row][col] = 1 if board[row][col] > 0 else 0



if __name__ == "__main__":
    matrix = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Solution().gameOfLife(matrix)
    print(f"Solution is {matrix}")

    matrix = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
    Solution2().gameOfLife(matrix)
    print(f"Solution with O(1) space complexity is {matrix}")

    matrix = [[1,1],[1,0]]
    Solution().gameOfLife(matrix)
    print(f"Solution is {matrix}")

    matrix = [[1,1],[1,0]]
    Solution2().gameOfLife(matrix)
    print(f"Solution with O(1) space complexity is {matrix}")

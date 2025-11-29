from typing import List


class SolutionDFS:
    """
    Notes
    -----
    - TC: O(m * n)
    - SC: O(m * n)
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
        m, n = len(board), len(board[0])

        def dfs(row, col):
            if not (0 <= row < m and 0 <= col < n):
                return
            if board[row][col] != "O":
                return
            board[row][col] = "visited"
            for dx, dy in directions:
                new_row, new_col = row + dx, col + dy
                dfs(new_row, new_col)

        def flip(region):
            for row, col in region:
                board[row][col] = "X"

        # Iterate over the borders and perform DFS
        for row in range(m):
            for col in range(n):
                if (row in (0, m - 1) or col in (0, n - 1)) and board[row][col] == "O":
                    dfs(row, col)

        # Flip 'O's to 'X' in regions that are not visited during DFS
        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    flip(
                        [
                            (i, j)
                            for i in range(m)
                            for j in range(n)
                            if board[i][j] == "O"
                        ]
                    )

        # Change 'visited' back to 'O'
        for row in range(m):
            for col in range(n):
                if board[row][col] == "visited":
                    board[row][col] = "O"


class SolutionDFS2:
    """
    Notes
    -----
    - TC: O(m * n)
    - SC: O(m * n)
    """

    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m, n = len(board), len(board[0])
        directions = ((0, 1), (0, -1), (1, 0), (-1, 0))

        def dfs(row, col):
            if 0 <= row < m and 0 <= col < n and board[row][col] == "O":
                board[row][col] = "visited"
                for dx, dy in directions:
                    new_r, new_c = row + dx, col + dy
                    dfs(new_r, new_c)

        for row in range(m):
            for col in range(n):
                if (row in {0, m - 1} or col in {0, n - 1}) and board[row][col] == "O":
                    dfs(row, col)

        for row in range(m):
            for col in range(n):
                if board[row][col] == "O":
                    board[row][col] = "X"
                elif board[row][col] == "visited":
                    board[row][col] = "O"


if __name__ == "__main__":
    grid = [
        ["X", "X", "X", "X", "O"],
        ["X", "X", "O", "X", "O"],
        ["X", "X", "O", "O", "X"],
        ["O", "O", "X", "X", "O"],
    ]
    SolutionDFS().solve(grid)
    print(f"DFS: {grid}")

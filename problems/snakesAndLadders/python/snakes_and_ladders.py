from collections import deque
from typing import List, Tuple


class Solution:
    """
    Notes
    -----
    - TC: O(N)
      - N: the number of squares in the board.
    - SC: O(N)
    """

    @staticmethod
    def convert_boustrophedon(n, square) -> Tuple[int, int]:
        row = n - (square - 1) // n - 1
        column_offset = (square - 1) % n
        column = n - 1 - column_offset if (n - row) % 2 == 0 else column_offset
        return row, column

    @staticmethod
    def update_square(board: List[List[int]], square: int) -> int:
        row, column = Solution.convert_boustrophedon(len(board), square)
        return board[row][column] if board[row][column] != -1 else square

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n, destination, dice_sides = len(board), len(board) ** 2, 6
        queue, visited = deque([(1, 0)]), {1}

        while queue:
            current_square, step = queue.popleft()
            if current_square == destination:
                return step

            for dice in range(1, dice_sides + 1):
                next_square = current_square + dice
                if next_square > destination:
                    break
                elif next_square not in visited:
                    visited.add(next_square)
                    updated_square = Solution.update_square(board, next_square)
                    queue.append((updated_square, step + 1))
        return -1


if __name__ == "__main__":
    board = [
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 35, -1, -1, 13, -1],
        [-1, -1, -1, -1, -1, -1],
        [-1, 15, -1, -1, -1, -1],
    ]

    print(f"BFS Solution: {Solution().snakesAndLadders(board)}")

    board = [
        [-1, -1, 19, 10, -1],
        [2, -1, -1, 6, -1],
        [-1, 17, -1, 19, -1],
        [25, -1, 20, -1, -1],
        [-1, -1, -1, -1, 15],
    ]

    print(f"BFS Solution: {Solution().snakesAndLadders(board)}")

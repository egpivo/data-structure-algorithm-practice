from collections import deque
from typing import List, Tuple


class Solution:
    @staticmethod
    def convert_to_boustrophedon(n, move) -> Tuple[int, int]:
        row = n - (move - 1) // n - 1
        right_forward = (move - 1) % n
        left_forward = n - right_forward - 1
        column = left_forward if (n - row) % 2 == 0 else right_forward
        return row, column

    @staticmethod
    def update_square(board: List[List[int]], square: int) -> int:
        row, column = Solution.convert_to_boustrophedon(len(board), square)
        return board[row][column] if board[row][column] != -1 else square

    def snakesAndLadders(self, board: List[List[int]]) -> int:
        n = len(board)
        destination = n**2

        queue = deque([(1, 0)])
        visited = set([1])

        while queue:
            current_square, step = queue.popleft()
            if current_square == destination:
                return step

            for dice in range(1, 7):
                next_square = current_square + dice
                if next_square > destination:
                    break
                elif next_square not in visited:
                    visited.add(next_square)
                    updated_square = self.update_square(board, next_square)
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

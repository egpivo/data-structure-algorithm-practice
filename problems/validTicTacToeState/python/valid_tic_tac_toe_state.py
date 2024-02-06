from typing import List


class Solution:
    def validTicTacToe(self, board: List[str]) -> bool:
        def check_winner(player):
            for row in board:
                if row.count(player * 3) == 1:
                    return True
            for col in zip(*board):
                if "".join(col).count(player * 3) == 1:
                    return True
            if (
                board[0][0] == board[1][1] == board[2][2] == player
                or board[0][2] == board[1][1] == board[2][0] == player
            ):
                return True
            return False

        x_count = sum(row.count("X") for row in board)
        o_count = sum(row.count("O") for row in board)

        if o_count not in {x_count, x_count - 1}:
            return False

        if check_winner("X") and x_count != o_count + 1:
            return False

        if check_winner("O") and x_count != o_count:
            return False

        return True


if __name__ == "__main__":
    board = ["XOX", "O O", "XOX"]
    print(f"{Solution().validTicTacToe(board)}")

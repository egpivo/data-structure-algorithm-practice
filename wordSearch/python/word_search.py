from typing import List


class Solution:
    """

    Complexity
    ----------
    - N: # of cells
    - L: length of a word
    - TC: O(N * 3 ^L)
    - SC: O(L)
    """

    direction = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        self.nrows = len(board)
        self.ncols = len(board[0])
        self.board = board

        for row in range(self.nrows):
            for col in range(self.ncols):
                if self.backtrack(row, col, word):
                    return True

        return False

    def backtrack(self, board, row, col, word) -> bool:
        if len(word) == 0:
            return True

        if not (0 <= row < self.nrows) or not (0 <= col < self.ncols) or self.board[row][col] != word[0]:
            return False

        does_exist = False
        self.board[row][col] = "#"
        for row_offset, col_offset in self.direction:
            does_exist = self.backtrack(row + row_offset, col + col_offset, word[1:])
            if does_exist:
                break

        self.board[row][col] = word[0]
        return does_exist


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    word2 = "ABCCES"
    print(f"{Solution().exist(board, word)}")
    print(f"{Solution().exist(board, word2)}")
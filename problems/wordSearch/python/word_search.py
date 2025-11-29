from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(m\cdot n \cdot 4^\text{len(word)})$
       - In the worst case, the algorithm explores all possible paths on the board, making it $O(m\cdot n \cdot 4^\text{len(word)})$, $m$ and $n$ are the dimensions of the board.
       - $4^\text{len(word)}$ represents the number of possible directions at each step.
    -  Space complexity:$O(\text{len(word)})$
       - It's due to the recursion stack. The depth of the recursion is limited by the length of the word.
    """

    def exist(self, board: List[List[str]], word: str) -> bool:
        m, n = len(board), len(board[0])
        directions = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        def backtrack(row: int, col: int, index: int) -> bool:
            if index == len(word):
                return True
            if not (0 <= row < m and 0 <= col < n and board[row][col] == word[index]):
                return False

            board[row][col] = "visited"
            temp = word[index]

            for dx, dy in directions:
                if backtrack(row + dx, col + dy, index + 1):
                    return True
            board[row][col] = temp

            return False

        for row in range(m):
            for col in range(n):
                if backtrack(row, col, 0):
                    return True

        return False


if __name__ == "__main__":
    board = [["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]]
    word = "ABCCED"
    word2 = "ABCCES"
    print(f"{Solution().exist(board, word)}")
    print(f"{Solution().exist(board, word2)}")

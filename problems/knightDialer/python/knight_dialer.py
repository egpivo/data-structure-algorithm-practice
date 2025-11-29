class Solution:
    """
    Complexity
    ----------
    -  Time complexity: $O(n \times 10^k)$
        - $k$ is the number of possible moves for each position.
        - This is because we iterate over all the positions on the board, which are 10 in total, and for each position, we recursively explore all the valid moves, which are at most 8 in total.
        - The `visited` dictionary helps to reduce the number of recursive calls by returning the cached results, but it does not change the asymptotic complexity.
    - Space complexity: $O(n \times 10^k)$
        - This is because we need to store the results for each position and index in the visited dictionary, which has at most $n * 10^k$ entries.
    """

    def knightDialer(self, n: int) -> int:
        nrows, ncols = 4, 3
        board = [[1, 1, 1], [1, 1, 1], [1, 1, 1], [0, 1, 0]]
        directions = (
            (1, 2),
            (1, -2),
            (-1, 2),
            (-1, -2),
            (2, 1),
            (2, -1),
            (-2, 1),
            (-2, -1),
        )
        modulo = 10**9 + 7

        memo = {}

        def dfs(position, index):
            nonlocal memo
            if index == n:
                return 1

            if (position, index) in memo:
                return memo[(position, index)]

            count = 0
            for dx, dy in directions:
                new_r = position[0] + dx
                new_c = position[1] + dy
                if 0 <= new_r < nrows and 0 <= new_c < ncols and board[new_r][new_c]:
                    count = (count + dfs((new_r, new_c), index + 1)) % modulo

            memo[(position, index)] = count
            return count

        result = 0
        for i in range(nrows):
            for j in range(ncols):
                if board[i][j] == 1:
                    result = (result + dfs((i, j), 1)) % modulo

        return result


if __name__ == "__main__":
    print(f"The answer is {Solution().knightDialer(2)}")

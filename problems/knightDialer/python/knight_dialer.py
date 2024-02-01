class Solution:
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

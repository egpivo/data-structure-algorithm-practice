class Solution:
    def checkRecord(self, n: int) -> int:
        MOD = 10**9 + 7

        if n == 0:
            return 1
        if n == 1:
            return 3

        # dp[i][j][k] represents the count of sequences of length i
        # where j is the count of 'A's and k is the count of trailing 'L's
        dp = [[[0] * 3 for _ in range(2)] for _ in range(n + 1)]

        # Base case: One sequence of length 0 with 0 'A's and 0 trailing 'L's
        dp[0][0][0] = 1

        for i in range(1, n + 1):
            for j in range(2):
                for k in range(3):
                    # Adding 'P'
                    dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j][k]) % MOD
                    # Adding 'A'
                    if j == 1:
                        dp[i][j][0] = (dp[i][j][0] + dp[i - 1][j - 1][k]) % MOD
                    # Adding 'L'
                    if k < 2:
                        dp[i][j][k + 1] = (dp[i][j][k + 1] + dp[i - 1][j][k]) % MOD

        total = 0
        for j in range(2):
            for k in range(3):
                total = (total + dp[n][j][k]) % MOD

        return total


if __name__ == "__main__":
    n = 10000
    print(f"Solution: {Solution().checkRecord(n)}")

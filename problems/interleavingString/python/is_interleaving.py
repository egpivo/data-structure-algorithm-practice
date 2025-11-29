class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        n, m = len(s1), len(s2)

        if len(s3) != n + m:
            return False

        if n == 0 or m == 0:
            return s1 + s2 == s3

        dp = [[False] * (m + 1) for _ in range(n + 1)]
        dp[0][0] = True

        # Check s1
        for i in range(n):
            dp[i + 1][0] = dp[i][0] and s1[i] == s3[i]
            if not dp[i + 1][0]:
                break

        # Check s2
        for j in range(m):
            dp[0][j + 1] = dp[0][j] and s2[j] == s3[j]
            if not dp[0][j + 1]:
                break

        # Check interleaving
        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = (dp[i][j + 1] and s1[i] == s3[i + j + 1]) or (
                    dp[i + 1][j] and s2[j] == s3[i + j + 1]
                )

        return dp[-1][-1]


if __name__ == "__main__":
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    print(f"Solution: {Solution().isInterleave(s1, s2, s3)}")

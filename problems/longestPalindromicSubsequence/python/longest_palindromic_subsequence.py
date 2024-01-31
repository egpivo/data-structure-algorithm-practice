class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) <= 1:
            return len(s)

        dp = [[0] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            dp[i][i] = 1
            for j in range(i + 1, len(s)):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][len(s) - 1]


if __name__ == "__main__":
    s = "bbbab"
    print(f"Palindromic subsequence is: {Solution().longestPalindromeSubseq(s)}")

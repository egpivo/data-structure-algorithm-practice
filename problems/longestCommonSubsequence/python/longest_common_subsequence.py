class Solution:
    """
    Complexity
    ----------
    - TC: O(m*n)
    - SC: O(m*n)
    """

    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        m, n = len(text1), len(text2)
        dp = [[0] * (m + 1) for _ in range(n + 1)]

        for i in range(n):
            for j in range(m):
                dp[i + 1][j + 1] = (
                    dp[i][j] + 1
                    if text1[j] == text2[i]
                    else max(dp[i][j + 1], dp[i + 1][j])
                )
        return dp[-1][-1]


if __name__ == "__main__":
    text1 = "abcde"
    text2 = "ace"
    print(f"{Solution().longestCommonSubsequence(text1, text2)}")

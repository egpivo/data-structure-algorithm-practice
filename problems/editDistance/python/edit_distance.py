class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n1, n2 = len(word1), len(word2)

        dp = [[0] * (n2 + 1) for _ in range(n1 + 1)]

        for i in range(n1 + 1):
            dp[i][0] = i
            for j in range(1, n2 + 1):
                if i == 0:
                    dp[i][j] = j
                elif word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1]
                else:
                    dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        return dp[-1][-1]


if __name__ == "__main__":
    word1 = "horse"
    word2 = "ros"
    print(f"Solution: {Solution().minDistance(word1, word2)}")

class Solution:
    """
    Complexity
    ----------
    - TC: O(n^3/2)
    - SC: O(n)
    """

    def numSquares(self, n: int) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                dp[i] = min(dp[i], dp[i - j * j] + 1)
                j += 1
        return dp[-1]


if __name__ == "__main__":
    print(f"Solution: {Solution().numSquares(12)}")

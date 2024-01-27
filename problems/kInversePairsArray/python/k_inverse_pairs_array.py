class Solution:
    """
    Complexity
    ----------
    - TC: O(n * k)
    - SC: O(n * k)
    """

    def kInversePairs(self, n: int, k: int) -> int:
        modulo = 10**9 + 7

        dp = [[0] * (k + 1) for _ in range(n + 1)]

        # Base case: dp[i][0] = 1 for all i
        for i in range(n + 1):
            dp[i][0] = 1

        for i in range(1, n + 1):
            window_sum = dp[i][0]  # Initialize window sum
            for j in range(1, k + 1):
                window_sum += dp[i - 1][j]
                if j >= i:
                    window_sum -= dp[i - 1][
                        j - i
                    ]  # Remove leftmost element from the window
                dp[i][j] = window_sum % modulo

        return dp[-1][-1] % modulo


if __name__ == "__main__":
    ans = Solution()
    print(f"The answer is {ans.kInversePairs(3, 1)}")

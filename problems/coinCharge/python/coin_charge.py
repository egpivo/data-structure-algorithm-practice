from typing import List


class Solution:
    """
    Note
    ----
    - DP: min_{k=0, \dots, n - 1} F(i - c_j) + 1

    Complexity
    ----------
    - Time: O(amount * n)
    - Space: O(amount) 
    - n = # of coints
    """

    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] = min(dp[i], dp[i - coin] + 1)

        return -1 if dp[-1] == float("inf") else dp[-1]


if __name__ == "__main__":
    coins = [1,2,5]
    amount = 11
    print(f"Solution: {Solution().coinChange(coins, amount)}")

from typing import List


class SolutionGreedy:
    def maxProfit(self, prices: List[int]) -> int:
        result = 0
        prev = prices[0]
        for price in prices[1:]:
            if price - prev > 0:
                result += price - prev
            prev = price
        return result


class SolutionDP:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)

        if n < 2:
            return 0

        # Create a DP array to store maximum profits at each day
        dp = [0] * n

        for i in range(1, n):
            # The maximum profit at day i is the maximum of:
            # 1. The profit obtained by selling at day i (prices[i] - prices[i-1])
            # 2. The profit obtained on the previous day (dp[i-1])
            dp[i] = max(dp[i - 1] + prices[i] - prices[i - 1], dp[i - 1])

        return dp[-1]


class SolutionDP2:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if n < 2:
            return 0

        # dp[i][j]: maximum profit on day i with j transactions
        dp = [[0] * 2 for _ in range(n)]

        # Base case: on day 0, no transactions, profit is 0
        dp[0][0] = 0
        # On day 0, if we buy a stock, profit is -prices[0]
        dp[0][1] = -prices[0]

        for i in range(1, n):
            # Either do nothing (no transaction) or sell the stock
            dp[i][0] = max(dp[i - 1][0], dp[i - 1][1] + prices[i])
            # Either do nothing (no transaction) or buy the stock
            dp[i][1] = max(dp[i - 1][1], dp[i - 1][0] - prices[i])

        # The maximum profit is in the last day with no stock in hand
        return max(dp[-1][0], 0)


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Solution: {SolutionGreedy().maxProfit(prices)}")
    print(f"Solution: {SolutionDP().maxProfit(prices)}")
    print(f"Solution: {SolutionDP2().maxProfit(prices)}")

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


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Solution: {SolutionGreedy().maxProfit(prices)}")

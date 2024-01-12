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


if __name__ == "__main__":
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Solution: {SolutionGreedy().maxProfit(prices)}")

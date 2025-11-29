class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    _memo = {-1: 0, 0: 0, 1: 1, 2: 1}

    def tribonacci(self, n: int) -> int:
        if n in self._memo:
            return self._memo[n]

        self._memo[n] = self.tribonacci(n - 1) * 2 - self.tribonacci(n - 4)
        return self._memo[n]


class SolutionBottomUp:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def tribonacci(self, n: int) -> int:
        if n == 0:
            return 0
        elif n <= 2:
            return 1
        dp = [0] * (n + 2)

        dp[2] = 1
        dp[3] = 1
        for i in range(4, n + 2):
            dp[i] = dp[i - 1] * 2 - dp[i - 4]
        return dp[-1]


if __name__ == "__main__":
    num = 101
    print(f"The solution is {Solution().tribonacci(num)}")
    print(f"The solution is {SolutionBottomUp().tribonacci(num)}")

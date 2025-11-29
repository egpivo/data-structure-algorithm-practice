class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n
        current = previous = 1
        for _ in range(n - 1):
            current, previous = current + previous, current

        return current


class SolutionDP:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def climbStairs(self, n: int) -> int:
        if n <= 3:
            return n

        dp = [0] * (n + 1)
        dp[1], dp[2] = 1, 2
        for i in range(3, n + 1):
            dp[i] = dp[i - 1] + dp[i - 2]
        return dp[-1]


if __name__ == "__main__":
    n = 6
    print(f"Solution: {Solution().climbStairs(n)}")
    print(f"Solution: {Solution().climbStairs(n)}")

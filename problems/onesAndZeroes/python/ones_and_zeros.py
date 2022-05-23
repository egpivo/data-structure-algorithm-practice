from functools import cache
from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time: O(mnk)
    - Space: O(mnk)
    """

    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        xy = [[s.count("0"), s.count("1")] for s in strs]

        @cache
        def dp(m, n, k):
            if m < 0 or n < 0:
                return float("-inf")
            if k == len(strs):
                return 0
            x, y = xy[k]
            return max(1 + dp(m - x, n - y, k + 1), dp(m, n, k + 1))

        return dp(m, n, 0)


if __name__ == "__main__":
    strs = ["10", "0001", "111001", "1", "0"]
    m = 5
    n = 3
    print(f"Solution: {Solution().findMaxForm(strs, m, n)}")

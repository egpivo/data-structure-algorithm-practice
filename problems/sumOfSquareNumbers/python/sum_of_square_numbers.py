import math


class Solution:
    """
    Complexity
    ----------
    - TC: O(\sqrt(c))
    - SC: O(1)
    """

    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(math.sqrt(c))

        while left <= right:
            total = left**2 + right**2

            if total == c:
                return True
            elif total < c:
                left += 1
            else:
                right -= 1

        return False


if __name__ == "__main__":
    c = 5
    print(Solution().judgeSquareSum(c))

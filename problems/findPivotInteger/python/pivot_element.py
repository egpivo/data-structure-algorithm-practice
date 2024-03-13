class Solution:
    """
    Complexity
    ----------
    - TC: O(\log n)
    - SC: O(1)
    """

    def pivotInteger(self, n: int) -> int:
        left, right = 1, n

        while left <= right:
            mid = left + (right - left) // 2
            mid_left = self.sum_arithmetic_series(1, mid)
            mid_right = self.sum_arithmetic_series(mid, n)

            if mid_left == mid_right:
                return mid
            elif mid_left > mid_right:
                right -= 1
            else:
                left += 1

        return -1

    def sum_arithmetic_series(self, a1: int, an: int) -> int:
        # Formula for the sum of an arithmetic series: (n / 2) * (a1 + an)
        return (an - a1 + 1) * (a1 + an) // 2


if __name__ == "__main__":
    num = 8
    print(f"The solution is {Solution().pivotInteger(num)}")

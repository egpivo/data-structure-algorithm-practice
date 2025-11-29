class Solution:
    """
    Complexity
    ----------
    - TC: O(log(x))
    - SC: O(1)
    """

    def mySqrt(self, x: int) -> int:
        if x <= 1:
            return x

        left, right = 0, x

        while left <= right:
            mid = left + (right - left) // 2
            estimate = mid * mid
            if estimate == x:
                return mid
            elif estimate > x:
                right = mid - 1
            else:
                left = mid + 1

        return left - 1


if __name__ == "__main__":
    print(f"{Solution().mySqrt(8)}")

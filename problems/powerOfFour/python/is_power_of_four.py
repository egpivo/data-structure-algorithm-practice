class Solution:
    """
    Complexity
    ----------
    - TC: O(\log n)
    - SC: O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is positive
        if n <= 0:
            return False

        # Check if n is a power of 4
        while n > 1:
            if n % 4 != 0:
                return False
            n >>= 2

        return True


class Solution2:
    """
    Complexity
    ----------
    - TC: O(1)
    - SC: O(1)
    """

    def isPowerOfFour(self, n: int) -> bool:
        # Check if n is positive and a power of 4
        return n > 0 and n & (n - 1) == 0 and n & 0xAAAAAAAA == 0


if __name__ == "__main__":
    num = 101
    print(f"The solution is {Solution().isPowerOfFour(num)}")
    print(f"The solution is {Solution2().isPowerOfFour(num)}")

class Solution:
    """
    Complexity
    ----------
    - TC: O(\log(n))
    - SC: O(1)
    """

    def isPowerOfTwo(self, n: int) -> bool:
        if n <= 0:
            return False

        ones_count = 0
        while n:
            ones_count += n & 1
            n >>= 1
            if ones_count > 1:
                return False

        return ones_count == 1


if __name__ == "__main__":
    num = 101
    print(f"The solution is {Solution().isPowerOfTwo(num)}")

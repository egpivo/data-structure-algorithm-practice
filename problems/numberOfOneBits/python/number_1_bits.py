class Solution:

    """
    Complexity
    ----------
    - Time: O(1)
    - Space: O(1)
    """

    def hammingWeight(self, n: int) -> int:
        return sum((n & (1 << i)) != 0 for i in range(32))


class Solution2:
    def hammingWeight(self, n: int) -> int:
        m = 31
        count = 0

        while n > 0:
            count += n & 1
            n >>= 1
            m -= 1
        return count


if __name__ == "__main__":
    n = 11
    print(f"Solution: {Solution().hammingWeight(n)}")

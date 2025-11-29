class Solution:
    """
    Notes
    -----
        - If n is 101010 in binary, then `n & 1` will be 0.
        - If n is 101011 in binary, then `n & 1` will be 1.
        - If `last_digit` is 101 in binary, and m is 2, then last_digit << m will be 10100 in binary, which is equivalent to 4 in decimal.
    """

    def reverseBits(self, n: int) -> int:
        m = 31
        result = 0

        while n > 0:
            last_digit = n & 1
            result += last_digit << m
            n >>= 1
            m -= 1

        return result

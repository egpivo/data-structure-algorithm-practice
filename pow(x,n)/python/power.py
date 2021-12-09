class Solution:
    """
    Complexity
    ----------
    - TC: O(log n)
    - SC: O(1)
    """
    def power(self, x: float, n: int) -> float:
        answer = self._recurse(x, n)
        return answer if n >= 0 else 1 / answer

    def _recurse(self, base: int, exponent: int) -> float:
        if exponent == 0:
            return 1

        if exponent % 2 == 0:
            return self._recurse(base * base, (abs(exponent)) // 2)
        else:
            return base * self._recurse(base * base, (abs(exponent) - 1) // 2)


if __name__ == "__main__":
    x = 2.00000
    n = -2
    print(f"Solution: {Solution().power(x, n)}")

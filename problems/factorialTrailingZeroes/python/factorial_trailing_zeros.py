class Solution:
    def trailingZeroes(self, n: int) -> int:
        "ans = quotient + quotient // 5"
        quotient = n // 5
        return quotient + self.trailingZeroes(quotient) if quotient > 0 else quotient


if __name__ == "__main__":
    print(f"Solution: {Solution().trailingZeroes(5)}")

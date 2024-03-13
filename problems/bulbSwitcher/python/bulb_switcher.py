class Solution:
    def bulbSwitch(self, n: int) -> int:
        # Only perfect squares have an odd number of factors
        # Thus, the result is the square root of the count of perfect squares up to n
        return int(n**0.5)


if __name__ == "__main__":
    print(f"Solution: {Solution().bulbSwitch(4)}")

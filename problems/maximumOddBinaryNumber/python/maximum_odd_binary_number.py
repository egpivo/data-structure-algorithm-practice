class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def maximumOddBinaryNumber(self, s: str) -> str:
        ones_count = s.count("1")
        n = len(s)

        if ones_count > 0:
            return "1" * (ones_count - 1) + "0" * (n - ones_count) + "1"
        else:
            return s


if __name__ == "__main__":
    s = "0101"
    print(f"The answer is {Solution().maximumOddBinaryNumber(s)}")

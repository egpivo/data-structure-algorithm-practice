class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def scoreOfString(self, s: str) -> int:
        return sum(abs(ord(s[i]) - ord(s[i + 1])) for i in range(len(s) - 1))


if __name__ == "__main__":
    s = "string"
    print(f"The solution is {Solution().scoreOfString(s)}")

class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return s
        reversed_s = s[::-1]

        for i in range(len(reversed_s)):
            if s.startswith(reversed_s[i:]):
                return reversed_s[:i] + s


if __name__ == "__main__":
    print(f"Solution: {Solution().shortestPalindrome(s)}")

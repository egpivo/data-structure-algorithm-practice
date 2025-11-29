from collections import Counter


class Solution:
    def longestPalindrome(self, s: str) -> int:
        max_len = sum(
            freq - 1 if freq % 2 != 0 else freq for freq in Counter(s).values()
        )
        return max_len + 1 if max_len < len(s) else max_len


if __name__ == "__main__":
    s = "abccccdd"
    print(f"Palindromic subsequence is: {Solution().longestPalindrome(s)}")

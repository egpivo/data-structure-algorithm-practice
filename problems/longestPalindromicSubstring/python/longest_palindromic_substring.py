class Solution:
    def longestPalindrome(self, s):
        """
        Complexity
        ----------
        - TC: O(n^2)
        - SC: O(1)
        """
        n = len(s)
        if n < 2: return s

        start = end = 0

        for i in range(n - 1):
            start, end = self.searchPalindrome(s, i, i, start, end)
            start, end = self.searchPalindrome(s, i, i + 1, start, end)

        return s[start:(start + end)]

    def searchPalindrome(self, s, left, right, start, end):

        while (left >= 0) and (right < len(s)) and (s[left] == s[right]):
            left -= 1
            right += 1

        if end < right - left - 1:
            start = left + 1
            end = right - left - 1

        return start, end


class SolutionDP:
    """
    Complexity
    ----------
    - TC: O(n^2)
    - SC: O(n^2)
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [[False] * n for _ in range(n)]
        result = ""
        max_length = 0

        for end in range(n):
            for start in range(end + 1):

                if start == end:
                    dp[start][end] = True
                elif start + 1 == end:
                    dp[start][end] = s[start] == s[end]
                else:
                    dp[start][end] = s[start] == s[end] and dp[start + 1][end - 1]

                if dp[start][end] and end - start + 1 > max_length:
                    max_length = end - start + 1
                    result = s[start: end + 1]

        return result


class SolutionDP2:
    """
    Complexity
    ----------
    - TC: O(n^2)
    - SC: O(n)
    """
    def longestPalindrome(self, s: str) -> str:
        n = len(s)

        dp = [False]* n
        result = ""

        for end in range(n):
            for start in range(end + 1):

                if start == end:
                    dp[start] = True
                elif start + 1 == end:
                    dp[start] = s[start] == s[end]
                else:
                    dp[start] = s[start] == s[end] and dp[start + 1]

                if dp[start] and end - start + 1 > len(result):
                    result = s[start: end + 1]

        return result



if __name__ == "__main__":
    s = "babad"

    print(f"Palindromic substing is: {Solution().longestPalindrome(s)}")
    print(f"Palindromic substing is: {SolutionDP().longestPalindrome(s)}")
    print(f"Palindromic substing is: {SolutionDP2().longestPalindrome(s)}")
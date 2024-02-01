class Solution:
    """
    Complexity
    ----------
    - Time: O(N^3)
    - Space: O(1)
    """

    def countSubstrings(self, s: str) -> int:
        answer = 0

        for left in range(len(s)):
            right = len(s) - 1
            while left <= right:
                if self.is_palindromic(s, left, right):
                    answer += 1
                right -= 1

        return answer

    def is_palindromic(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True


class DPSolution:
    """
    Complexity
    ----------
    - Time: O(N^2)
    - Space: O(N^2)
    """

    def countSubstrings(self, s: str) -> int:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        answer = n

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            dp[i][i + 1] = s[i] == s[i + 1]
            answer += dp[i][i + 1]

        for win in range(3, n + 1):
            for i in range(n - win + 1):
                j = i + win - 1
                dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
                answer += dp[i][j]

        return answer


class SolutionDFS:
    def countSubstrings(self, s: str) -> int:
        count = 0

        def is_palindromic(substring):
            return substring == substring[::-1]

        def dfs(index):
            nonlocal count
            if index == len(s):
                return

            for i in range(index, len(s)):
                substring = s[index : i + 1]
                if is_palindromic(substring):
                    count += 1

            dfs(index + 1)

        dfs(0)
        return count


if __name__ == "__main__":
    s = "aaa"
    print(f"Solution: {Solution().countSubstrings(s)}")
    print(f"DPSolution: {Solution().countSubstrings(s)}")
    print(f"DFSolution: {Solution().countSubstrings(s)}")

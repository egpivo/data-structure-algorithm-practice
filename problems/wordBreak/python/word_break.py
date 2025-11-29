from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        # Initialize a DP array to track whether a substring can be broken into words
        dp = [False] * (len(s) + 1)
        dp[0] = True  # Empty string is always breakable

        for i in range(1, len(s) + 1):
            for word in wordDict:
                # Check if the current substring ending at position i can be broken
                if (
                    i >= len(word)
                    and dp[i - len(word)]
                    and s[i - len(word) : i] == word
                ):
                    dp[i] = True
                    break
        return dp[-1]


if __name__ == "__main__":
    s = "leetcode"
    wordDict = ["leet", "code"]
    print(f"{Solution().wordBreak(s, wordDict)}")

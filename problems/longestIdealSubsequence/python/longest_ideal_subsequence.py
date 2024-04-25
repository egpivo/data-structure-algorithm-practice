class Solution:
    """
    Complexity
    ----------

    - TC: O(n)
    - SC: O(1)
    """

    def longestIdealString(self, s: str, k: int) -> int:
        bound_map = {}

        # Create bounds for unique characters in s
        for char in set(s):
            char_ord = ord(char)
            if char not in bound_map:
                lower_bound = max(ord("a"), char_ord - k) - ord("a")
                upper_bound = min(ord("z"), char_ord + k) - ord("a") + 1
                bound_map[char] = (lower_bound, upper_bound)

        # Calculate the longest ideal string length for each character
        dp = [0] * 26
        for char in s:
            lower_bound, upper_bound = bound_map[char]
            max_prev_len = max(dp[lower_bound:upper_bound])
            dp[ord(char) - ord("a")] = max_prev_len + 1

        # Return the maximum length of the ideal string
        return max(dp)


if __name__ == "__main__":
    s = "acfgbd"
    k = 2
    print(f"The solution is {Solution().longestIdealString(s, k)}")

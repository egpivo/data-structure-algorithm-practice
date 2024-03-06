class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def minimumLength(self, s: str) -> int:
        left, right = 0, len(s) - 1

        while left < right and s[left] == s[right]:
            current_char = s[left]

            # Skip consecutive characters from the left
            while left <= right and s[left] == current_char:
                left += 1

            # Skip consecutive characters from the right
            while left <= right and s[right] == current_char:
                right -= 1

        return max(0, right - left + 1)


if __name__ == "__main__":
    s = "aabccabba"
    print(f"{Solution().minimumLength(s)}")

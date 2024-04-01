class Solution:
    """
    Complexity
    ----------
    - Time complexity: O(n)
    - Space complexity: O(1)
    """

    def lengthOfLastWord(self, s: str) -> int:
        # Split the string by spaces and get the last word,
        # then return its length
        return len(s.split()[-1])


if __name__ == "__main__":
    s = "Hello World"

    print(f"Solution: {Solution().lengthOfLastWord(s)}")

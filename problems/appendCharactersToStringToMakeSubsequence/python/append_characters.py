class Solution:
    """
    Complexity
    ----------
    - TC: O(n + m)
    - SC: O(1)
    """

    def appendCharacters(self, s: str, t: str) -> int:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
            else:
                i += 1
        return len(t) - j


if __name__ == "__main__":
    s = "coaching"
    t = "coding"
    print(f"The output: {Solution().appendCharacters(s, t)}")

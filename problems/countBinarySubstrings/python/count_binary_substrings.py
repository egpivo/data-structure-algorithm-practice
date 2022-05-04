class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(len(s) - 1):
            if s[i] != s[i + 1]:
                groups.append(1)
            else:
                groups[-1] += 1

        return sum(min(groups[i], groups[i + 1]) for i in range(len(groups) - 1))


if __name__ == "__main__":
    s = "00110011"
    print(f"{Solution().countBinarySubstrings(s)}")

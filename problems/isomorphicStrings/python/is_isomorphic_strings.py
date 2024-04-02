class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s)) == len(set(t)) == len(set(zip(s, t)))


if __name__ == "__main__":
    s = "egg"
    t = "add"
    print(f"Solution: {Solution().isIsomorphic(s, t)}")

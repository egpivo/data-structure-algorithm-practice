from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(\max(N \log N, M \log M))$
    - Space complexity: $O(1)
    """

    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        if not g or not s:
            return 0

        g.sort()
        s.sort()

        child_index, cookie_index = 0, 0

        while child_index < len(g) and cookie_index < len(s):
            if s[cookie_index] >= g[child_index]:
                child_index += 1
            cookie_index += 1

        return child_index


if __name__ == "__main__":
    g = [1, 2, 3]
    s = [1, 1]
    print(f"The Solution is {Solution().findContentChildren(g, s)}")

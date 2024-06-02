from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def reverse(self, s: List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1


if __name__ == "__main__":
    s = ["h", "e", "l", "l", "o"]
    ans = Solution()
    ans.reverse(s)
    print(f"The output: {s}")

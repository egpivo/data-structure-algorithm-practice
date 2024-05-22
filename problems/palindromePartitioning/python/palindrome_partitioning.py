from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n 2^n)
    - SC: O(n 2^n)
    """

    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(sub: str) -> bool:
            return sub == sub[::-1]

        def backtrack(left: int, path: List[str]):
            if left == len(s):
                result.append(path)
                return
            for right in range(left + 1, len(s) + 1):
                substring = s[left:right]
                if is_palindrome(substring):
                    backtrack(right, path + [substring])

        result = []
        backtrack(0, [])
        return result


if __name__ == "__main__":
    s = "aab"
    print(f"Solution: {Solution().partition(s)}")

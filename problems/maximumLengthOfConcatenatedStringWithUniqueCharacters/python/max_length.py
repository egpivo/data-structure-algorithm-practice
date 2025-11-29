from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(2^n)
    - SC: O(2^n)
    """

    def maxLength(self, arr: List[str]) -> int:
        def backtrack(index, path):
            nonlocal max_length

            if len(path) != len(set(path)):
                return

            max_length = max(max_length, len(path))

            for i in range(index, len(arr)):
                backtrack(i + 1, path + arr[i])

        max_length = 0
        backtrack(0, "")
        return max_length


if __name__ == "__main__":
    arr = ["a", "abc", "d", "de", "def"]
    print(f"{Solution().maxLength(arr)} \narr = {arr}")

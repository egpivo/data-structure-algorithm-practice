from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations = []

        def backtrack(path, index):
            if len(path) > k:
                return
            elif len(path) == k:
                combinations.append(path.copy())
                return

            for number in range(index, n + 1):
                path.append(number)
                backtrack(path, number + 1)
                path.pop()

        backtrack([], 1)
        return combinations


if __name__ == "__main__":
    n = 5
    k = 2

    print(f"Solution: {Solution().combine(n, k)}")

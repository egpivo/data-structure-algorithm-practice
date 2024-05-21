from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n 2^n)
    - SC: O(n 2^n)
    """

    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrack(index: int, path: List[int]):
            result.append(path[:])
            for i in range(index, len(nums)):
                backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(Solution().subsets(nums))

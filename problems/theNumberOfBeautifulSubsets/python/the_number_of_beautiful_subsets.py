from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n 2^n)
    - SC: O(n)
    """

    def beautifulSubsets(self, nums: List[int], k: int) -> int:
        nums.sort()
        count = 0

        def backtrack(index, path):
            nonlocal count
            if index > len(nums):
                return

            if path:
                count += 1

            for i in range(index, len(nums)):
                if nums[i] - k not in path:
                    backtrack(i + 1, path + [nums[i]])

        backtrack(0, [])
        return count


if __name__ == "__main__":
    nums = [2, 4, 6]
    print(f"The solution is {Solution().beautifulSubsets(nums)}")

from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path, indexces):
            nonlocal result
            if len(path) == len(nums):
                if path not in result:
                    result.append(path)
                return

            for i in range(len(nums)):
                if i not in indexces:
                    backtrack(path[:] + [nums[i]], indexces[:] + [i])

        result = []
        for i in range(len(nums)):
            backtrack([nums[i]], [i])
        return result


if __name__ == "__main__":
    nums = [1, 2, 3]
    print(f"Solution is: {Solution().permuteUnique(nums)}")

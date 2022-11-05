from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            if not 0 < nums[i] <= n:
                nums[i] = n + 1
        
        for i in range(n):
            index = abs(nums[i])
            if 0 < index <= n:
                nums[index - 1] = - abs(nums[index - 1])
        
        for i in range(n):
            if nums[i] > 0:
                return i + 1

        return n + 1


if __name__ == "__main__":
    nums = [3,4,-1,1]
    print(f"Solution: {Solution().firstMissingPositive(nums)}")


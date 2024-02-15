from typing import List


class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()

        prefix_sum = [nums[0]]
        for num in nums[1:]:
            prefix_sum.append(prefix_sum[-1] + num)

        max_len = -1
        for i in range(1, n - 1):
            if prefix_sum[i] > nums[i + 1]:
                max_len = prefix_sum[i + 1]
        return max_len


if __name__ == "__main__":
    nums = [1, 12, 1, 2, 5, 50, 3]
    print(f"Solution: {Solution().largestPerimeter(nums)}")

class Solution:
    def maxSubarraySumCircular(self, nums):
        local_max = global_max = float("-inf")
        local_min = global_min = float("inf")

        total = 0
        for num in nums:
            local_max = max(local_max + num, num)
            global_max = max(global_max, local_max)

            local_min = min(local_min + num, num)
            global_min = min(global_min, local_min)

            total += num

        return max(global_max, total - global_min) if global_max > 0 else global_max


if __name__ == "__main__":
    nums = [5, -3, 5]
    print(f"Solution: {Solution().maxSubarraySumCircular(nums)}")

from typing import List


class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        difference = float('inf')
        nums_length = len(nums)

        nums.sort()
        for i in range(nums_length):
            low, high = i + 1, nums_length - 1
            while low < high:
                total  = nums[i] + nums[low] + nums[high]
                if abs(target - total) < abs(difference):
                    difference = target - total
                if total < target:
                    low += 1
                else:
                    high -= 1
            if difference == 0:
                break
        return target - difference
     

if __name__ == "__main__":
  nums = [-1,2,1,-4]
  target = 1

  print(Solution().threeSumClosest(nums, target))

from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        
        Note
        ----
        - Two pointer scheme
        - time: O(N)
        - space: O(1)
        """
        index = 0
        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0 and nums[slow] == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                
            if nums[slow] != 0:
                slow +=1


if __name__ == "__main__":
    nums = [0,1,0,3,12]
    Solution().moveZeroes(nums)
    print(nums)

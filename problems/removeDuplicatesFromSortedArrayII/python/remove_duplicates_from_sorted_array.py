from typing import List


class Solution:
    def removeDuplicatesII(self, nums: List[int]) -> int:
        """
        Complexity
        ----------
        - SC: O(n)
        - TC: O(1)
        """
        count = 1
        prev = nums[0]
        left = 0
        right = 1

        while right < len(nums):
            if nums[right] != prev:
                nums[count] = nums[right]
                count += 1
                left = right
            elif right - left <= 1:
                nums[count] = nums[right]
                count += 1
            prev = nums[right]
            right += 1
        return count


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    print(f"{Solution().removeDuplicatesII(nums)} \nnums = {nums}")

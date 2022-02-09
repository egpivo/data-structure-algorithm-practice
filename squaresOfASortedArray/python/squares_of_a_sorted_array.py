from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(N)
    - SC: O(1)
    """
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left, right = 0, len(nums) - 1

        answer = []
        while 0 <= left <= right < len(nums):
            if abs(nums[left]) < abs(nums[right]):
                answer.append(nums[right] ** 2)
                right -= 1
            else:
                answer.append(nums[left] ** 2)
                left += 1
        return answer[::-1]

if __name__ == "__main__":
    nums = [-4,-1,0,3,10]
    print(f"{Solution().sortedSquares(nums)}")
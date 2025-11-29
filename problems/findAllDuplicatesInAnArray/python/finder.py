from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def findDuplicates(self, nums: List[int]) -> List[int]:
        result = []

        for num in nums:
            abs_num = abs(num)
            if nums[abs_num - 1] < 0:
                result.append(abs_num)
            else:
                nums[abs_num - 1] *= -1

        return result


if __name__ == "__main__":
    nums = [4, 3, 2, 7, 8, 2, 3, 1]
    print(f"The solution is {Solution().findDuplicates(nums)}")

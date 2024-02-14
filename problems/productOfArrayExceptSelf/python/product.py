from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        total = 1
        zeros = 0
        last_zero_index = None

        for index, num in enumerate(nums):
            if num != 0:
                total *= num
            else:
                zeros += 1
                last_zero_index = index

        answer = [0] * n

        if zeros == 1:
            answer[last_zero_index] = total
        elif zeros == 0:
            for index, num in enumerate(nums):
                answer[index] = total // num
        return answer


if __name__ == "__main__":
    nums = [1, 2, 3, 4]
    print(f"Solution: {Solution().productExceptSelf(nums)}")

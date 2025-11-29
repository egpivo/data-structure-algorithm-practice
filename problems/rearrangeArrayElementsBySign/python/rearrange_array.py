from collections import deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - SC: O(n)
    - TC: O(n)
    """

    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positive_nums = deque([num for num in nums if num > 0])
        negative_nums = deque([num for num in nums if num <= 0])

        result = []
        while positive_nums or negative_nums:
            result.append(positive_nums.popleft())
            result.append(negative_nums.popleft())

        return result


if __name__ == "__main__":
    nums = [3, 1, -2, -5, 2, -4]
    print(f"The Solution is {Solution().rearrangeArray(nums)}")

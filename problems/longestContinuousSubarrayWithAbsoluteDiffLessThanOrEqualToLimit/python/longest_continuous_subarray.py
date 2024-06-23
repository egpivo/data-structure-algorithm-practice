from collections import deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def longestSubarray(self, nums: List[int], limit: int) -> int:
        max_deque = deque()
        min_deque = deque()
        left = 0
        max_len = 0

        for right in range(len(nums)):
            while max_deque and nums[right] > nums[max_deque[-1]]:
                max_deque.pop()
            max_deque.append(right)

            while min_deque and nums[right] < nums[min_deque[-1]]:
                min_deque.pop()
            min_deque.append(right)

            while nums[max_deque[0]] - nums[min_deque[0]] > limit:
                left += 1
                if max_deque[0] < left:
                    max_deque.popleft()
                if min_deque[0] < left:
                    min_deque.popleft()

            max_len = max(max_len, right - left + 1)

        return max_len


if __name__ == "__main__":
    nums = [8, 2, 4, 7]
    limit = 4
    print(f"{Solution().longestSubarray(nums, limit)}")

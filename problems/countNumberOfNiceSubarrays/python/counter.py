from collections import defaultdict
from typing import List


class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        odd_count = 0
        prefix_count = defaultdict(int)
        prefix_count[0] = 1
        result = 0

        for num in nums:
            odd_count += num % 2

            if odd_count - k in prefix_count:
                result += prefix_count[odd_count - k]

            prefix_count[odd_count] += 1

        return result


if __name__ == "__main__":
    nums = [1, 1, 2, 1, 1]
    k = 3
    print(f"{Solution().numberOfSubarrays(nums, k)}")

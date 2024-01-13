from collections import Counter
from typing import List


class Solution:
    def minOperations(self, nums: List[int]) -> int:
        if not nums:
            return -1

        num_count = Counter(nums)
        if min(num_count.values()) < 2:
            return -1

        total_operations = 0
        for freq in num_count.values():
            while freq >= 2:
                if freq % 3 == 0:
                    total_operations += freq // 3
                    freq = 0
                else:
                    freq -= 2
                    total_operations += 1
            if freq != 0:
                return -1

        return total_operations


if __name__ == "__main__":
    nums = [1, 2, 3, 1]
    print(f"Solution: {Solution().minOperations(nums)}")

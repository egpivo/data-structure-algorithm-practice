from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(m)
    """

    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        freq = defaultdict(int)
        freq[0] = 1
        prefix_sum = 0
        result = 0

        for num in nums:
            prefix_sum += num
            remainder = prefix_sum % k

            if remainder < 0:
                remainder += k

            if remainder in freq:
                result += freq[remainder]

            freq[remainder] += 1

        return result


if __name__ == "__main__":
    nums = [4, 5, 0, -2, -3, 1]
    k = 5
    print(f"The solution is {Solution().subarraysDivByK(nums, k)}")

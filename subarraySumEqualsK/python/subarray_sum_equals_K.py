from typing import List
from collections import defaultdict


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Heuristic (c.f. two sum)
        ---------
        - Example: nums = [1, 1, 1]; k = 2
        - Start from 0
            1. index 0: cumulative sum = 1; distance(k, sum(nums[0:1])): 1 - 2 = -1
            2. index 1: cumulative sum = 2; distance(k, sum(nums[0:2])): 2 - 2 = 0
            3. index 2: cumulative sum = 3; distance(k, sum(nums[0:3])): 3 - 2 = 1
        - Start from 1
            1. index 1: cumulative sum = 1; distance(k, sum(nums[1:2])): 1 - 2 = -1
            2. index 2: cumulative sum = 2; distance(k, sum(nums[1:3)): 2 - 2 = 0
        - Start from 2
            1. index 2: cumulative sum = 1; distance(k, sum(nums[2:3])): 1 - 2 = -1

        ---> sum[i, j] = sum[i,] - sum[j,] for any i < j
        ---> objective: find sum[i, j] == k  <==> sum[i,] - sum[j,] == k <==> sum[j, ] ==  sum[i, ] - k
        ---> create a hash map for the cumulative sum begin at index i and its occurrence

        Complexity
        ----------
        - TC: O(N)
        - SC: O(N)
        """
        hash_map = defaultdict(int)
        hash_map[0] = 1

        total = 0
        count = 0
        for num in nums:
            total += num
            if hash_map.get(total - k):
                count += hash_map[total - k]
            hash_map[total] += 1
        return count


if __name__ == "__main__":
    nums = [1, 1, 1]
    k = 2
    output = Solution().subarraySum(nums, k)
    assert output == 2, f"Wrong answer, but got {output}"

    nums = [1, -1, 2, -2, 3, -3, 2, 2]
    k = 0
    output = Solution().subarraySum(nums, k)
    assert output == 7, f"Wrong answer, but got {output}"

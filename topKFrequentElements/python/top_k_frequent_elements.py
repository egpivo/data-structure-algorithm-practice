import heapq
from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(nlog(n))
    - SC: O(n + k)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = sorted(freq, key=freq.get, reverse=True)
        return sorted_freq[:k]


class SolutionHeap:
    """
    Complexity
    ----------
    - TC: O(nlog(k))
    - SC: O(n + k)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        if len(nums) <= k:
            return nums
        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"{Solution().topKFrequent(nums, k)}")
    print(f"{SolutionHeap().topKFrequent(nums, k)}")

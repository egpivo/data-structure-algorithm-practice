from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(nlog(n))
    - SC: O(n)
    """

    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = sorted(freq, key=lambda x: freq.get(x), reverse=True)
        return sorted_freq[:k]


if __name__ == "__main__":
    nums = [1, 1, 1, 2, 2, 3]
    k = 2
    print(f"{Solution().topKFrequent(nums, k)}")

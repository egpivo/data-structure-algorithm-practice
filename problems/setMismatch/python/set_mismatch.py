from collections import Counter
from typing import List


class Solution:
    """
    Notes
    -----
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def findErrorNums(self, nums: List[int]) -> List[int]:
        nums_freq = Counter(nums)
        result = [nums_freq.most_common(1)[0][0], None]

        for i in range(1, len(nums) + 1):
            if i not in nums_freq:
                result[-1] = i
                break
        return result


if __name__ == "__main__":
    arr = [3, 1, 2, 4, 4]
    print(f"{Solution().findErrorNums(arr)}")

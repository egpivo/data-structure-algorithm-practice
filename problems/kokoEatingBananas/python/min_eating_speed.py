import math
from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: O(n\log{m})
       - n is the number of piles and mmm is the maximum number of bananas in a pile.
       - Each binary search iteration takes O(n)) time to calculate the total time spent at a certain eating speed.
       - Binary search iterates \log(m) times.
    - Space complexity: O(1)
    """

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        left, right = 1, max(piles) + 1

        while left < right:
            mid = left + (right - left) // 2
            spent = sum(math.ceil(pile / mid) for pile in piles)
            if spent > h:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    piles = [30, 11, 23, 4, 20]
    h = 5

    print(f"The answer is {Solution().minEatingSpeed(piles, h)}")

from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n \log(\text{max\_day} - \text{min\_day})).
    - SC: O(1)
    """

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m * k:
            return -1

        left, right = min(bloomDay), max(bloomDay)

        while left < right:
            mid = (left + right) // 2
            if self._canMakeBouquets(mid, bloomDay, m, k):
                right = mid
            else:
                left = mid + 1

        return left

    def _canMakeBouquets(self, days, bloomDay, m, k):
        bouquets = 0
        flowers = 0
        for day in bloomDay:
            if day <= days:
                flowers += 1
                if flowers == k:
                    bouquets += 1
                    flowers = 0
            else:
                flowers = 0
            if bouquets >= m:
                return True
        return bouquets >= m


if __name__ == "__main__":
    bloomDay = [1, 10, 3, 10, 2]
    m = 3
    k = 1
    print(f"The solution is {Solution().minDays(bloomDay, m, k)}")

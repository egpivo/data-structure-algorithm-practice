from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def maximumHappinessSum(self, happiness: List[int], k: int) -> int:
        happiness.sort(reverse=True)

        result = 0
        for decrease, value in enumerate(happiness):
            if k == 0 or value - decrease < 0:
                break
            result += value - decrease
            k -= 1

        return result


if __name__ == "__main__":
    happiness = [1, 2, 87, 87, 87, 2, 1]
    k = 3

    print(f"The solution is {Solution().maximumHappinessSum(happiness, k)}")

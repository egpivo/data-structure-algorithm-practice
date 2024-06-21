from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def maxSatisfied(
        self, customers: List[int], grumpy: List[int], minutes: int
    ) -> int:
        n = len(customers)

        base_satisfaction = sum(customers[i] for i, gr in enumerate(grumpy) if gr == 0)
        potential_increase = sum(customers[i] for i in range(minutes) if grumpy[i] == 1)

        max_increase = potential_increase
        for i in range(minutes, n):
            if grumpy[i] == 1:
                potential_increase += customers[i]
            if grumpy[i - minutes] == 1:
                potential_increase -= customers[i - minutes]

            max_increase = max(max_increase, potential_increase)

        return base_satisfaction + max_increase


if __name__ == "__main__":
    customers = [1, 0, 1, 2, 1, 1, 7, 5]
    grumpy = [0, 1, 0, 1, 0, 1, 0, 1]
    minutes = 3
    print(f"{Solution().maxSatisfied(customers, grumpy, minutes)}")

from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log n)
    - SC: O(1)
    """

    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left, right = 0, len(people) - 1
        boats_needed = 0

        # Iterate until the pointers meet or cross each other
        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            right -= 1

            boats_needed += 1

        # Return the total count of boats needed
        return boats_needed


if __name__ == "__main__":
    people = [3, 2, 2, 1]
    limit = 3
    print(f"The solution is {Solution().numRescueBoats(people, limit)}")

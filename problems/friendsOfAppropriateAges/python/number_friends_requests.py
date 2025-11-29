from collections import Counter
from typing import List


class Solution:
    def numFriendRequests(self, ages: List[int]) -> int:
        age_counts = Counter(ages)
        total_requests = 0

        for age_y, count_y in age_counts.items():
            for age_x, count_x in age_counts.items():
                if age_y > 0.5 * age_x + 7 and age_y <= age_x:
                    total_requests += count_y * count_x

                    # If the ages are the same, we need to subtract the requests
                    # from the same person
                    if age_y == age_x:
                        total_requests -= count_x

        return total_requests


if __name__ == "__main__":
    ages = [20, 30, 100, 110, 120]
    print(f"Solution: {Solution().numFriendRequests(ages)}")

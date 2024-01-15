from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        winner_count = defaultdict(int)
        loser_count = defaultdict(int)

        for winner, loser in matches:
            winner_count[winner] += 1
            loser_count[loser] += 1

        no_lose_winners = [
            winner for winner in winner_count if loser_count[winner] == 0
        ]
        one_lose_winners = [loser for loser, count in loser_count.items() if count == 1]

        return [sorted(no_lose_winners), sorted(one_lose_winners)]


if __name__ == "__main__":
    matches = [
        [1, 3],
        [2, 3],
        [3, 6],
        [5, 6],
        [5, 7],
        [4, 5],
        [4, 8],
        [4, 9],
        [10, 4],
        [10, 9],
    ]
    print(f"Solution: {Solution().findWinners( matches)}")

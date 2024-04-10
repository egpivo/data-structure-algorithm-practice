from collections import deque
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log n)
    - SC: O(n)
    """

    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse=True)
        result = deque()
        for card in deck:
            if result:
                result.appendleft(result.pop())
            result.appendleft(card)
        return list(result)


if __name__ == "__main__":
    deck = [17, 13, 11, 2, 3, 5, 7]
    print(f"The solution is {Solution().deckRevealedIncreasing(deck)}")

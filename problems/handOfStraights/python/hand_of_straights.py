import heapq
from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n \log(k))
    - SC: O(n)
    """

    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        if len(hand) % groupSize != 0:
            return False

        # Create a counter for the frequencies of each card
        freq = Counter(hand)

        # Create a min-heap from the keys of the counter
        min_heap = list(freq.keys())
        heapq.heapify(min_heap)

        while min_heap:
            min_card = min_heap[0]
            for i in range(min_card, min_card + groupSize):
                if freq[i] == 0:
                    return False
                freq[i] -= 1
                if freq[i] == 0:
                    # Remove the card from the heap if its count drops to zero
                    if i != min_heap[0]:
                        return False
                    heapq.heappop(min_heap)

        return True


if __name__ == "__main__":
    hand = [1, 2, 3, 6, 2, 3, 4, 7, 8]
    groupSize = 3

    print(f"The solution is {Solution().isNStraightHand(hand, groupSize)}")

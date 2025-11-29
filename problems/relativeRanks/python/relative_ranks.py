from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log n)
    - SC: O(n)
    """

    def findRelativeRanks(self, score: List[int]) -> List[str]:
        # Enumerate the scores to get indices and sort them in descending order
        sorted_indices = sorted(range(len(score)), key=lambda x: score[x], reverse=True)
        result = [""] * len(score)
        medal_map = {0: "Gold Medal", 1: "Silver Medal", 2: "Bronze Medal"}

        # Assign ranks to the top three scores directly and store the rest in a list
        for rank, index in enumerate(sorted_indices):
            result[index] = medal_map.get(rank, str(rank + 1))

        return result


if __name__ == "__main__":
    score = [10, 3, 8, 9, 4]

    print(Solution().findRelativeRanks(score))

from collections import deque
from typing import List


class Solution:
    """
    Notes
    -----
    - TC: O(NM)
      - $N$: Length of the gene sequence.
      - $M$: Number of possible choices (4, in this case).
    - SC: O(N)
    """

    @staticmethod
    def mutate(gene: str, choice: str, position: int) -> str:
        return gene[:position] + choice + gene[position + 1 :]

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        bank = set(bank)
        choices = set("ACGT")
        queue = deque([(startGene, 0)])
        visited = set(startGene)

        while queue:
            gene, step = queue.popleft()
            for position in range(len(gene)):
                for choice in choices:
                    mutation = Solution.mutate(gene, choice, position)
                    if mutation == endGene:
                        return step + 1
                    elif mutation not in visited and mutation in bank:
                        visited.add(mutation)
                        queue.append((mutation, step + 1))
        return -1


if __name__ == "__main__":
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]

    print(f"BFS Solution: {Solution().minMutation(startGene, endGene, bank)}")

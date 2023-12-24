from collections import deque
from typing import List


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        if endGene not in bank:
            return -1

        choices = ("A", "C", "G", "T")
        queue = deque([(startGene, 0)])
        visited = set()
        while queue:
            gene, step = queue.popleft()
            for position in range(len(startGene)):
                for choice in choices:
                    mutation = gene[:position] + choice + gene[position + 1 :]
                    if mutation in bank and mutation not in visited:
                        if mutation == endGene:
                            return step + 1
                        visited.add(mutation)
                        queue.append((mutation, step + 1))
        return -1


if __name__ == "__main__":
    startGene = "AACCGGTT"
    endGene = "AAACGGTA"
    bank = ["AACCGATT", "AACCGATA", "AAACGATA", "AAACGGTA"]

    print(f"BFS Solution: {Solution().minMutation(startGene, endGene, bank)}")

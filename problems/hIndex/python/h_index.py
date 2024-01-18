from typing import List


class Solution:
    def hIndex(self, citations: List[int]) -> int:
        if len(citations) == 0:
            return 0
        elif len(citations) == 1:
            return 1 if citations[0] > 0 else 0

        citations.sort(reverse=True)
        # case: [11,15]
        if citations[-1] >= len(citations):
            return len(citations)

        for index, citation in enumerate(citations):
            if index + 1 > citation:
                return index

        return 0


class SolutionDP:
    def hIndex(self, citations: List[int]) -> int:
        n = len(citations)
        dp = [0] * (n + 1)

        for citation in citations:
            dp[min(n, citation)] += 1

        h_index = 0
        papers = 0
        for i in range(n, 0, -1):
            papers += dp[i]
            if papers >= i:
                h_index = papers
                break
        return h_index


if __name__ == "__main__":
    print(f"{Solution().hIndex([3,0,6,1,5])}")
    print(f"{SolutionDP().hIndex([3,0,6,1,5])}")

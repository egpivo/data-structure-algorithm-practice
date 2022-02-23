from typing import List


class Solution:
    """
    Complexity
    ----------
    TC: O(N)
    SC: O(N)
    """
    window = 10

    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        n = len(s)

        if n < self.window:
            return []

        answer, seen = set(), set()

        for i in range(n - self.window + 1):
            seq = s[i:i + self.window]

            if seq in seen:
                answer.add(seq)
            else:
                seen.add(seq)

        return answer


if __name__ == '__main__':
    s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
    ans = Solution()
    print(f"Solution: {ans.findRepeatedDnaSequences(s)}")

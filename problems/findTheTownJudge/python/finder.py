from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: O(E+n)
        - E be the number of trust relationships in the input (edge)
    - Space complexity: O(n)
    """

    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        trust_count = [0] * (n + 1)

        for src, dst in trust:
            trust_count[
                src
            ] -= 1  # decrement trust count for the person making the trust
            trust_count[
                dst
            ] += 1  # increment trust count for the person receiving the trust

        for person in range(1, n + 1):
            if trust_count[person] == n - 1:
                return person

        return -1  # no judge found


if __name__ == "__main__":
    n = 3
    trust = [[1, 3], [2, 3]]
    print(f"The solution is {Solution().findJudge(n, trust)}")

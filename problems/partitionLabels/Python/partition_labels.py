from typing import List


class Solution:
    """

    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def partitionLabels(self, s: str) -> List[int]:
        last = {char: index for index, char in enumerate(s)}

        j = anchor = 0
        answer = []

        for index, char in enumerate(s):
            j = max(last[char], j)
            if index == j:
                answer.append(j - anchor + 1)
                anchor = index + 1

        return answer


if __name__ == "__main__":
    s = "ababcbacadefegdehijhklij"

    print(f"{Solution().partitionLabels(s)}")

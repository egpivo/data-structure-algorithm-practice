from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: O(nlogn)
        - n is the number of tokens.
        - The dominant factor is the sorting of the tokens.
    - Space complexity: O(1)
    """

    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        n = len(tokens)
        tokens.sort()
        left, right = 0, n - 1
        score, max_score = 0, 0

        while left <= right:
            if tokens[left] <= power:
                power -= tokens[left]
                score += 1
                left += 1
                max_score = max(max_score, score)
            elif score > 0:
                power += tokens[right]
                score -= 1
                right -= 1
            else:
                break

        return max_score


if __name__ == "__main__":
    tokens = [100, 200, 300, 400]
    power = 200

    print(f"Solution: {Solution().bagOfTokensScore(tokens, power)}")

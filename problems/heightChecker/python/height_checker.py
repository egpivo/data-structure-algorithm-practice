from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log(n))
    - SC: O(n)
    """

    def heightChecker(self, heights: List[int]) -> int:
        expected_heights = sorted(heights)
        mismatch_count = sum(
            1
            for original, expected in zip(heights, expected_heights)
            if original != expected
        )
        return mismatch_count


if __name__ == "__main__":
    heights = [1, 1, 4, 2, 1, 3]
    print(f"The solution is {Solution().heightChecker(heights)}")

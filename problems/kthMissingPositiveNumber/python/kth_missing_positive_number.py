from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(\log(n))
    - SC: O(1)
    """

    def findKthPositive(self, arr: List[int], k: int) -> int:
        left, right = 0, len(arr) - 1

        while left <= right:
            mid = left + (right - left) // 2
            num_miss = arr[mid] - (mid + 1)

            if num_miss >= k:
                right = mid - 1
            else:
                left = mid + 1

        return left + k


class SolutionIterative:
    """
    Complexity
    ----------
    - TC: O(log n)
    - SC: O(1)
    """

    def power(self, x: float, n: int) -> float:

        answer = 1
        exponent = abs(n)
        base = x
        while exponent > 0:
            if exponent & 1:
                answer *= base
            base = base * base
            exponent >>= 1
        return answer if n >= 0 else 1 / answer


if __name__ == "__main__":
    x = 2.00000
    n = -2
    print(f"Solution: {Solution().power(x, n)}")
    print(f"Solution: {SolutionIterative().power(x, n)}")

from typing import List


class Solution:
    """
    Notes
    -----
    - Monotonic Stack

    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        result = 0
        mod_value = 10**9 + 7

        stack = [(0, arr[0])]

        for index, value in enumerate(arr[1:], 1):
            while stack and value <= stack[-1][1]:
                prev_index, min_value = stack.pop()
                prev_prev_index = stack[-1][0] if stack else -1
                result += (
                    min_value * (index - prev_index) * (prev_index - prev_prev_index)
                )

            stack.append((index, value))

        while stack:
            prev_index, min_value = stack.pop()
            prev_prev_index = stack[-1][0] if stack else -1
            result += min_value * (n - prev_index) * (prev_index - prev_prev_index)

        return result % mod_value


if __name__ == "__main__":
    arr = [3, 1, 2, 4]
    print(f"{Solution().sumSubarrayMins(arr)}")

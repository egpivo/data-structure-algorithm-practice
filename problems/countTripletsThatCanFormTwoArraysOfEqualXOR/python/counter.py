from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def countTriplets(self, arr: List[int]) -> int:
        n = len(arr)
        prefix = [0] * (n + 1)

        for i in range(n):
            prefix[i + 1] = prefix[i] ^ arr[i]

        count = defaultdict(int)
        total = defaultdict(int)
        result = 0

        for k in range(n):
            if prefix[k + 1] in count:
                result += count[prefix[k + 1]] * k - total[prefix[k + 1]]

            count[prefix[k]] += 1
            total[prefix[k]] += k

        return result


if __name__ == "__main__":
    arr = [2, 3, 1, 6, 7]

    print(f"Solution: {Solution().countTriplets(arr)}")

from collections import defaultdict
from typing import List


class Solution:
    """
    Note
    ----
    - TC: O(n)
    - SC: O(n)
    """

    def compute_longest_length(self, array: List[int], k: int) -> int:
        hash_map = defaultdict(int)
        prefix_sum = 0
        answer = 0

        for idx, num in enumerate(array):
            prefix_sum += num

            if prefix_sum == k:
                answer = idx + 1
            elif prefix_sum - k in hash_map:
                answer = max(answer, idx - hash_map[prefix_sum - k])
            if prefix_sum not in hash_map:
                hash_map[prefix_sum] = idx

        return answer


if __name__ == "__main__":
    array = [10, 5, 2, 7, 1, 9]
    k = 15
    print(f"{Solution().compute_longest_length(array, k)}")

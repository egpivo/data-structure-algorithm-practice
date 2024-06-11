import heapq
from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n + mk + p \log p)
        -n: the length of arr1
        -m is the length of arr2
        -k is the average frequency of each number in arr1.
        -p is the number of unique elements in arr1 not in arr2.
    - SC: O(n)
    """

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        freq = Counter(arr1)

        result = []
        for num in arr2:
            result.extend([num] * freq[num])
            del freq[num]

        for key in sorted(freq):
            result.extend([key] * freq[key])

        return result


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n\log n)
    - SC: O(n)
    """

    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        priority_queue = []
        array2_index = {key: index for index, key in enumerate(arr2)}

        for num in arr1:
            if num in arr2:
                heapq.heappush(priority_queue, (array2_index[num], num))
            else:
                heapq.heappush(priority_queue, (len(arr2), num))

        result = []
        while priority_queue:
            result.append(heapq.heappop(priority_queue)[1])

        return result


if __name__ == "__main__":
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]

    print(Solution().relativeSortArray(arr1, arr2))
    print(Solution2().relativeSortArray(arr1, arr2))

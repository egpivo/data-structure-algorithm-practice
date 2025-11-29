import bisect
from typing import List


class SparseVectorHashMap:
    """
    Note
    ----
    - n: the length of the input array
    - L: the number of non-zero elements.
    - Time complexity:
        - O(n): creating the Hash Map
        - O(L): calculating the dot product.
    - Space complexity:
        - O(L): the Hash Map
        - O(1): calculating the dot product.
    """

    def __init__(self, nums: List[int]):
        self.num_map = {index: val for index, val in enumerate(nums) if val != 0}

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        result = 0
        intersected_index = set(self.num_map).intersection(vec.num_map.keys())
        for index in intersected_index:
            result += vec.num_map[index] * self.num_map[index]

        return result


class SparseVectorTwoPointers:
    """
    Note
    ----
    - n: the length of the input array
    - L, L2: the number of non-zero elements for the two vectors
    - Time complexity:
        - O(n): creating the <index, value> pairs for non-zero values
        - O(L + L2): calculating the dot product.
    - Space complexity:
        - O(L): creating the <index, value> pairs for non-zero values
        - O(1): calculating the dot product.
    """

    def __init__(self, nums: List[int]):
        self.pairs = [(index, val) for index, val in enumerate(nums) if val != 0]

    def __len__(self) -> int:
        return len(self.pairs)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        result = 0
        left = 0
        right = 0
        while left < len(self) and right < len(vec):
            if self.pairs[left][0] == vec.pairs[right][0]:
                result += self.pairs[left][1] * vec.pairs[right][1]
                left += 1
                right += 1
            elif self.pairs[left][0] < vec.pairs[right][0]:
                left += 1
            else:
                right += 1
        return result


class SparseVectorTwoPointersBinarySearch:
    """
    Note
    ----
    - n: the length of the input array
    - L, L2: the number of non-zero elements for the two vectors
    - Time complexity:
        - O(n): creating the <index, value> pairs for non-zero values
        - O(L + L2): calculating the dot product.
    - Space complexity:
        - O(L): creating the <index, value> pairs for non-zero values
        - O(1): calculating the dot product.
    """

    def __init__(self, nums: List[int]):
        self.indcies = [index for index, val in enumerate(nums) if val != 0]
        self.vals = [val for val in nums if val != 0]

    def __len__(self) -> int:
        return len(self.indcies)

    # Return the dotProduct of two sparse vectors
    def dotProduct(self, vec: "SparseVector") -> int:
        result = 0
        left = 0
        right = 0
        while left < len(self) and right < len(vec):
            if self.indcies[left] == vec.indcies[right]:
                result += self.vals[left] * vec.vals[right]
                left += 1
                right += 1
            elif self.indcies[left] < vec.indcies[right]:
                left = bisect.bisect_left(self.indcies, vec.indcies[right], lo=left + 1)
            else:
                right += bisect.bisect_left(
                    self.indcies, self.indcies[left], lo=right + 1
                )
        return result


if __name__ == "__main__":
    nums1 = [1, 0, 0, 2, 3]
    nums2 = [0, 3, 0, 4, 0]
    v1 = SparseVectorHashMap(nums1)
    v2 = SparseVectorHashMap(nums2)
    print(v1.dotProduct(v2))

    v1 = SparseVectorTwoPointers(nums1)
    v2 = SparseVectorTwoPointers(nums2)
    print(v1.dotProduct(v2))

    v1 = SparseVectorTwoPointersBinarySearch(nums1)
    v2 = SparseVectorTwoPointersBinarySearch(nums2)
    print(v1.dotProduct(v2))

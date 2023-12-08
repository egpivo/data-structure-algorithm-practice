# Definition for singly-linked list.
from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.

        Notes
        -----
        TC: O(n+m)
        """
        i, j, k = m - 1, n - 1, n + m - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1

            k -= 1
        while j > 0:
            nums1[k] = nums2[j]
            k -= 1
            j -= 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3

    Solution().merge(nums1=nums1, m=m, nums2=nums2, n=n)
    print(nums1)

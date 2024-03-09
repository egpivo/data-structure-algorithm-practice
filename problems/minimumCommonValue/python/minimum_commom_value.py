from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(min(m, n))
    - SC: O(1)
    """

    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        index1 = index2 = 0

        while index1 < len(nums1) and index2 < len(nums2):
            if nums1[index1] == nums2[index2]:
                return nums1[index1]
            elif nums1[index1] > nums2[index2]:
                index2 += 1
            else:
                index1 += 1

        return -1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 6]
    nums2 = [2, 3, 4, 5]
    print(f"{Solution().getCommon(nums1, nums2)}")

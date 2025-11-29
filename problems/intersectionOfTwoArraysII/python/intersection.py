from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n+m)
    - SC: O(n)
    """

    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Ensure nums1 is the shorter list
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        # Count the frequency of elements in the shorter list
        freq_count_nums1 = Counter(nums1)

        # Initialize an empty list to store the intersection result
        intersection_result = []

        # Iterate over elements in the shorter list
        for num in nums2:
            # Check if the current element exists in the frequency count
            if num in freq_count_nums1 and freq_count_nums1[num] > 0:
                # Add the current element to the intersection result
                intersection_result.append(num)
                # Decrease the frequency count of the current element
                freq_count_nums1[num] -= 1

        return intersection_result


if __name__ == "__main__":
    num1 = [4, 5, 6, 7, 7]
    num2 = [7, 7, 7]

    print(Solution().intersect(num1, num2))

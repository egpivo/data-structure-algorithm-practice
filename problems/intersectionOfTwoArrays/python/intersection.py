from typing import List


class Solution1:
    """
    Complexity
    ----------
    - TC: O(n+m)
    - SC: O(n+m)
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        unique1 = set(nums1)
        unique2 = set(nums2)

        if unique1 > unique2:
            unique1, unique2 = unique2, unique1
        return [num for num in unique1 if num in unique2]


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n+m)
    - SC: O(n+m)
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1) & set(nums2))


class Solution3:
    """
    Complexity
    ----------
    - TC: O(n+m)
    - SC: O(n+m)
    """

    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1).intersection(nums2))


if __name__ == "__main__":
    num1 = [4, 5, 6, 7]
    num2 = [7, 7]

    print(Solution1().intersection(num1, num2))
    print(Solution2().intersection(num1, num2))
    print(Solution3().intersection(num1, num2))

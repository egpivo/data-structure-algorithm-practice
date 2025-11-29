class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m, n = len(nums1), len(nums2)
        if m > n:
            return findMedianSortedArrays(nums2, nums1)

        start, end = 0, m
        inf = 2**1000

        while start <= end:

            split1 = (end - start) / 2
            split2 = (m + n + 1) / 2 - split1

            maxLeft1 = -inf if split1 == 0 else nums1[split1 - 1]
            minRight1 = inf if split1 == m else nums1[split1]
            maxLeft2 = -inf if split2 == 0 else nums2[split2 - 1]
            minRight2 = inf if split2 == n else nums2[split2]

            if maxLeft1 <= minRight2 & maxLeft2 <= minRight1:
                return (
                    (max(maxLeft1, maxLeft2) + min(minRight1, minRight2)) / 2.0
                    if ((m + n) % 2 == 0)
                    else max(maxLeft1, maxLeft2)
                )
            elif maxLeft1 > minRight2:
                start = split1 + 1
            else:
                end = split1 - 1


if __name__ == "__main__":
    nums1 = [1, 2, 3, 4]
    nums2 = [5, 6, 7, 8]
    ans = Solution()
    print("The median is %.1f" % ans.findMedianSortedArrays(nums1, nums2))

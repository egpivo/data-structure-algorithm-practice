# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):


def calculate_mid(left, right):
    return left + (right - left) // 2


class Solution:
    def firstBadVersion(self, n):
        """
        :type n: int
        :rtype: int

        Note
        ----
        - binary search: O(log(n))
        - `python` `left + right` could overflow -> `left + (right - left)//2`
        """
        if not isBadVersion(n - 1) and isBadVersion(n):
            return n

        left = 1
        right = n
        mid = calculate_mid(left, right)

        while mid:
            if not isBadVersion(mid - 1) and isBadVersion(mid):
                return mid
            elif isBadVersion(mid):
                right = mid
            else:
                left = mid
            mid = calculate_mid(left, right)

class Solution:
    def isValid(self, cut_len, arr, k):
        count = 0
        for wood in arr:
            if wood >= cut_len:
                count += wood // cut_len
            else:
                return False
        return True if count >= k else False

    def cutWood(self, arr, k):
        left = 1
        right = max(arr)
        res = 0
        while left < right:
            mid = left + (right - left) // 2
            if self.isValid(mid, arr, k):
                res = mid
                left = mid + 1
            else:
                right = mid
        return res


if __name__ == "__main__":
    arr = [5, 9, 7]
    k = 4
    print(f"Solution: {Solution().cutWood(arr, k)}")

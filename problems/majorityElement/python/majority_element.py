from collections import Counter


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        for i in set(nums):
            if nums.count(i) > len(nums) / 2:
                return i

        return -1


# Moore voting
class Solution2:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count, mode = 1, nums[0]
        for val in nums[1:]:
            if val == mode:
                count += 1
            else:
                if count == 0:
                    mode = val
                    count = 1
                else:
                    count -= 1

        return mode


class Solution3:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def majorityElement(self, nums):
        freq = Counter(nums)
        return freq.most_common(1)[0][0]


if __name__ == "__main__":
    nums = [2, 2, 1, 1, 1, 2, 2]
    ans = Solution()
    print(ans.majorityElement(nums))
    ans2 = Solution2()
    print(ans2.majorityElement(nums))
    ans3 = Solution3()
    print(ans3.majorityElement(nums))

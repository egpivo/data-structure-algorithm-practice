class SolutionBruteForce:
    def lengthOfLongestSubstring(self, s: str) -> int:
        def is_duplicate(start: int, end: int) -> bool:
            chars = [0] * 128
            for i in range(start, end + 1):
                c = s[i]
                chars[ord(c)] += 1
                if chars[ord(c)] > 1:
                    return True
            return False

        n = len(s)
        res = 0
        for i in range(n):
            for j in range(i, n):
                if not is_duplicate(i, j):
                    res = max(res, j - i + 1)
        return res


class SolutionSlidingWindow:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        right = 0

        chars = [0] * 128
        max_len = len(s)
        ans = 0
        while right < max_len:
            r = s[right]
            chars[ord(r)] += 1

            while chars[ord(r)] > 1:
                l = s[left]
                chars[ord(l)] -= 1
                left += 1

            ans = max(ans, right - left + 1)
            right += 1

        return ans


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        temp = {}
        ans = 0
        idx = -1

        for i, char in enumerate(s):
            idx = max(idx, temp.get(char, -1))
            temp[char] = i
            ans = max(ans, i - idx)

        return ans


if __name__ == "__main__":
    test1 = "abcabcbb"
    test2 = "bbbbb"
    test3 = "pwwkew"

    detect = Solution()
    detect2 = SolutionBruteForce()
    detect3 = SolutionSlidingWindow()

    print(
        "Given %s  the length is %d" % (test1, detect.lengthOfLongestSubstring(test1))
    )
    print(
        "Given %s  the length is %d" % (test2, detect.lengthOfLongestSubstring(test2))
    )
    print(
        "Given %s  the length is %d" % (test3, detect.lengthOfLongestSubstring(test3))
    )

    print(
        "Given %s  the length is %d" % (test1, detect2.lengthOfLongestSubstring(test1))
    )
    print(
        "Given %s  the length is %d" % (test2, detect2.lengthOfLongestSubstring(test2))
    )
    print(
        "Given %s  the length is %d" % (test3, detect2.lengthOfLongestSubstring(test3))
    )

    print(
        "Given %s  the length is %d" % (test1, detect3.lengthOfLongestSubstring(test1))
    )
    print(
        "Given %s  the length is %d" % (test2, detect3.lengthOfLongestSubstring(test2))
    )
    print(
        "Given %s  the length is %d" % (test3, detect3.lengthOfLongestSubstring(test3))
    )

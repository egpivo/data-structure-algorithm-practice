
class Solution:
    def validPalindrome(self, s: str) -> bool:
        """
        Note
        ----
        - Time complexity: O(n)
        - Space complexity: O(1)
        """
        def is_valid(left: int, right: int, is_one_wrong: bool) -> bool:
            if left == right:
                return True

            while left < right:
                if is_one_wrong:
                    return False

                if s[left] != s[right]:
                    return is_valid(left + 1, right, True) or is_valid(left, right - 1, True)
                left += 1
                right -= 1
            return True
        return is_valid(0, len(s) - 1, False)

if __name__ == "__main__":
    s = "abca"

    print(Solution().validPalindrome(s))


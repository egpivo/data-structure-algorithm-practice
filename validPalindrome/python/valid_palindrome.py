class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Note
        ----
        - Time complexity: O(n)
        - Space complexity: O(n)
        """
        filtered_chars = filter(lambda char: char.isalnum(), s)
        lowercase_filtered_chars = map(lambda char: char.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]
        return filtered_chars_list == reversed_chars_list


class TwoPointerSolution:
    def isPalindrome(self, s: str) -> bool:
        """
        Note
        ----
        - Time complexity: O(n)
        - Space complexity: O(1)
        """
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1

            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"

    print(Solution().isPalindrome(s))
    print(TwoPointerSolution().isPalindrome(s))

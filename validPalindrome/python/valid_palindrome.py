class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered_chars = filter(lambda char: char.isalnum(), s)
        lowercase_filtered_chars = map(lambda char: char.lower(), filtered_chars)

        filtered_chars_list = list(lowercase_filtered_chars)
        reversed_chars_list = filtered_chars_list[::-1]
        return filtered_chars_list == reversed_chars_list


if __name__ == "__main__":
    s = "A man, a plan, a canal: Panama"

    print(Solution().isPalindrome(s))

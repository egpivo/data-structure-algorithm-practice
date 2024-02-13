from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n \times m)
        - n is the number of words in the list
        - m is the maximum length of the words.
    - SC: O(1)
    """

    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if word == word[::-1]:
                return word
        return ""


if __name__ == "__main__":
    words = ["abc", "car", "ada", "racecar", "cool"]
    print(f"The Solution is {Solution().firstPalindrome(words)}")

class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        len_word = len(word)
        start = num = 0

        for char in abbr:
            if char.isdigit():
                if num == 0 and char == "0":
                    return False
                num = num * 10 + int(char)
            else:
                start, num = start + num, 0
                if start >= len_word or word[start] != char:
                    return False
                start += 1

        return start + num == len_word


if __name__ == "__main__":
    word = "internationalization"
    abbr = "i12iz4n"

    print(Solution().validWordAbbreviation(word, abbr))

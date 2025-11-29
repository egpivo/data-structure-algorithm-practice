from typing import List


class Solution:
    def expressiveWords(self, s: str, words: List[str]) -> int:
        return sum(self.is_strechy(s, word) for word in words)

    def is_strechy(self, s: str, word: str) -> int:
        s_idx = w_idx = 0
        s_len = len(s)
        w_len = len(word)
        while s_idx < s_len and w_idx < w_len:
            s_count = 1
            while s_idx < s_len - 1 and s[s_idx] == s[s_idx + 1]:
                s_count += 1
                s_idx += 1
            w_count = 1
            while w_idx < w_len - 1 and word[w_idx] == word[w_idx + 1]:
                w_count += 1
                w_idx += 1

            if s[s_idx] != word[w_idx] or s_count < w_count:
                return 0

            s_idx += 1
            w_idx += 1

            if s_count == w_count:
                continue
            if s_count < 3:
                return 0

        return 1 if s_idx == s_len and w_idx == w_len else 0


if __name__ == "__main__":
    s = "heeellooo"
    words = ["hello", "hi", "helo"]
    print(f"{Solution().expressiveWords(s, words)}")

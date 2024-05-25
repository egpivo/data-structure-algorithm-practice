from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n 2^n)
    - SC: O(n^2)
    """

    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        word_set = set(wordDict)
        memo = {}

        def backtrack(index):
            if index == len(s):
                return [""]

            if index in memo:
                return memo[index]

            sentences = []
            for i in range(index, len(s)):
                word = s[index : i + 1]
                if word in word_set:
                    sub_sentences = backtrack(i + 1)
                    for sub_sentence in sub_sentences:
                        if sub_sentence:
                            sentences.append(word + " " + sub_sentence)
                        else:
                            sentences.append(word)

            memo[index] = sentences
            return sentences

        return backtrack(0)


if __name__ == "__main__":
    wordDict = ["cat", "cats", "and", "sand", "dog"]
    s = "catsanddog"
    print(f"Solution: {Solution().wordBreak(s, wordDict)}")

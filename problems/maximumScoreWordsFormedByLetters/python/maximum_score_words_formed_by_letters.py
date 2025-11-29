from collections import Counter
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(nm +  2^n m)
    - SC: O(n m)
    """

    def maxScoreWords(
        self, words: List[str], letters: List[str], score: List[int]
    ) -> int:
        word_counts = [Counter(word) for word in words]
        word_scores = [
            sum(score[ord(char) - ord("a")] for char in word) for word in words
        ]

        def backtrack(index, current_score, letter_count):
            nonlocal max_score

            if index == len(words):
                max_score = max(max_score, current_score)
                return

            # Skip the current word
            backtrack(index + 1, current_score, letter_count)

            # Try to use the current word if possible
            word_count = word_counts[index]
            can_use = all(letter_count[char] >= word_count[char] for char in word_count)

            if can_use:
                # Deduct letters used by the current word
                for char in word_count:
                    letter_count[char] -= word_count[char]

                # Include the current word's score and move to the next word
                backtrack(index + 1, current_score + word_scores[index], letter_count)

                # Restore the letter count
                for char in word_count:
                    letter_count[char] += word_count[char]

        max_score = 0
        letter_count = Counter(letters)
        backtrack(0, 0, letter_count)
        return max_score


if __name__ == "__main__":
    words = ["dog", "cat", "dad", "good"]
    letters = ["a", "a", "c", "d", "d", "d", "g", "o", "o"]
    score = [
        1,
        0,
        9,
        5,
        0,
        0,
        3,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        2,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
        0,
    ]
    print(f"The solution is {Solution().maxScoreWords(words, letters, score)}")

from collections import defaultdict


class Solution:
    """
    Complexity
    ----------
    - TC: O(nk)
    - SC: O(nk)
    - n: length of word
    - k: distinct number of characters
    """

    def wonderfulSubstrings(self, word: str) -> int:
        len(word)
        count = 0
        freq = defaultdict(int)
        freq[0] = 1  # Base case: empty substring

        num_bits = 10  # Number of bits used to encode characters

        curr_state = 0
        for char in word:
            curr_state ^= 1 << (ord(char) - ord("a"))  # Update the current state
            count += freq[curr_state]  # Count the wonderful substrings

            # Count the wonderful substrings with one extra character
            for i in range(num_bits):
                count += freq[curr_state ^ (1 << i)]

            freq[curr_state] += 1  # Update the frequency of the current state
        return count


if __name__ == "__main__":
    word = "aba"
    print(f"The Solution is {Solution().wonderfulSubstrings(word)}")

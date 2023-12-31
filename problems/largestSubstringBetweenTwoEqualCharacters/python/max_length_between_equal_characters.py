class Solution:
    """
    Notes
    -----
    - TC: O(n)
    - SC: O(n)
    """

    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_indices = {}
        max_distance = -1

        for index, char in enumerate(s):
            if char in char_indices:
                max_distance = max(max_distance, index - char_indices[char] - 1)
            else:
                char_indices[char] = index

        return max_distance


if __name__ == "__main__":
    print(f"{Solution().maxLengthBetweenEqualCharacters('abca')}")

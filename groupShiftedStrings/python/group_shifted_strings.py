from collections import defaultdict
from typing import List


class Solution:
    """
    Complexity
    ----------
    - n = # of strings
    - k = maximum length of a string
    - TC: O(n * k)
    - SC: O(n * k)
    """
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        string_order_map = defaultdict(list)

        for string in strings:
            order = []
            for char in string:
                value = ord(char) - ord(string[0])
                if value < 0:
                    value += 26
                order.append(value)
            string_order_map[tuple(order)].append(string)

        return [value for _, value in string_order_map.items()]


if __name__ == "__main__":
    strings = ["abc", "bcd", "acef", "xyz", "az", "ba", "a", "z"]

    print(Solution().groupStrings(strings))

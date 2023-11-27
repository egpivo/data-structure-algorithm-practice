from collections import defaultdict
from typing import List


class Solution:
    """
    Notes
    -----
    - TC: O(n*k*log(k))
    - SC: O(n * k)
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        answer_dict = defaultdict(list)

        for string in strs:
            key = "".join(sorted(string))
            answer_dict[key].append(string)
        return answer_dict.values()


if __name__ == "__main__":
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(f"Solution is {Solution().groupAnagrams(strs)}")

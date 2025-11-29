from typing import List


class Solution:
    """
    Complexity
    ----------
    - M: maximum length of a single list
    - N: # of logs in the list
    - TC: O(M Nlog(N))
        - O(N log(N)): `sorted` in python is based on Timsort algorithm
        - Since the keys of the elements are basically the logs itself, the comparison between two keys can take up to O(M) time.
    - SC: O(MN)
        - O(MN): `sorted` in python is based on Timsort algorithm
    """

    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        def get_key(log):
            identifier, rest_log = log.split(" ", maxsplit=1)
            # (indicator of the type of logs, content, id)
            # indicator of the type of logs = 0: letter log, 1: digit log
            return (0, rest_log, identifier) if rest_log[0].isalpha() else (1,)

        return sorted(logs, key=get_key)


if __name__ == "__main__":
    logs = [
        "dig1 8 1 5 1",
        "let1 art can",
        "dig2 3 6",
        "let2 own kit dig",
        "let3 art zero",
    ]
    print(f"The solution is {Solution().reorderLogFiles(logs)}")

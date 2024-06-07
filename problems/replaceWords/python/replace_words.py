from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(mn)
    - SC: O(m+n)
    """

    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        root_set = set(dictionary)
        tokens = sentence.split()

        # Replace tokens with the shortest root
        for i in range(len(tokens)):
            for root in sorted(root_set, key=len):
                if tokens[i].startswith(root):
                    tokens[i] = root
                    break

        return " ".join(tokens)


if __name__ == "__main__":
    dictionary = ["cat", "bat", "rat"]
    sentence = "the cattle was rattled by the battery"
    print(f"The solution is {Solution().replaceWords(dictionary, sentence)}")

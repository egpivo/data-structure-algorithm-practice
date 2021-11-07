class Solution:
    left_parenthesis = "("
    right_parenthesis = ")"

    def minRemoveToMakeValid(self, s: str) -> str:
        """ Broute force way

        Note
        ----
        - Time complexity: O(n)
        - Space complexity: O(n)
        """

        if not (self.left_parenthesis in s or self.right_parenthesis in s):
            return s

        removed_parenthesis_index = []
        left_parenthesis_count = 0

        for index, char in enumerate(s):
            if self.left_parenthesis == char:
                removed_parenthesis_index.append(index)
                left_parenthesis_count += 1
            if self.right_parenthesis == char:
                if removed_parenthesis_index and left_parenthesis_count > 0:
                    removed_parenthesis_index.pop()
                else:
                    removed_parenthesis_index.append(index)
        answer = []
        for index, char in enumerate(s):
            if not index in removed_parenthesis_index:
                answer.append(char)

        return "".join(answer)


if __name__ == "__main__":
    s = "lee(t(c)o)de)"
    print(f"Answer: {Solution().minRemoveToMakeValid(s)}")

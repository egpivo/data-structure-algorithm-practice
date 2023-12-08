from typing import List


class Solution:
    _left_bold_annotation = "<b>"
    _right_bold_annotation = "</b>"

    def addBoldTag(self, s: str, words: List[str]) -> str:
        s_size = len(s)
        is_bold_list = [False for i in range(s_size)]

        for word in words:
            start_index = s.find(word)
            while start_index != -1:
                for i in range(start_index, start_index + len(word)):
                    is_bold_list[i] = True
                start_index = s.find(word, start_index + 1)

        output = []
        index = 0
        is_left_bold_annotation = True
        while index < s_size:
            if is_bold_list[index]:
                if is_left_bold_annotation:
                    output.append(self._left_bold_annotation)
                    is_left_bold_annotation = False
            else:
                if not is_left_bold_annotation:
                    output.append(self._right_bold_annotation)
                    is_left_bold_annotation = True

            output.append(s[index])
            index += 1

        if not is_left_bold_annotation:
            output.append(self._right_bold_annotation)
        return "".join(output)


if __name__ == "__main__":
    s = "abcxyz123"
    words = ["abc", "123"]

    print(Solution().addBoldTag(s, words))

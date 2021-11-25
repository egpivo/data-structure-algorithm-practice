from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        n = len(num)
        answers = []

        def backtrack(index, pre_operand, cur_operand, value, path):
            if index == n:
                if value == target and cur_operand == 0:
                    answers.append("".join(path[1:]))

                return

            # NO OP
            cur_operand = cur_operand * 10 + int(num[index])
            str_cur_operand = str(cur_operand)
            if cur_operand > 0:
                backtrack(index + 1, pre_operand, cur_operand, value, path)

            # Addition
            path.append("+")
            path.append(str_cur_operand)
            backtrack(index + 1, cur_operand, 0, value + cur_operand, path)
            path.pop()
            path.pop()

            if path:
                # Subtraction
                path.append("-")
                path.append(str_cur_operand)
                backtrack(index + 1, -cur_operand, 0, value - cur_operand, path)
                path.pop()
                path.pop()

                # Multiplication
                path.append("*")
                path.append(str_cur_operand)
                backtrack(index + 1, cur_operand * pre_operand, 0, value - pre_operand + (pre_operand * cur_operand),
                          path)
                path.pop()
                path.pop()

        backtrack(0, 0, 0, 0, [])
        return answers


if __name__ == "__main__":
    num = "123"
    target = 6
    print(Solution().addOperators(num, target))

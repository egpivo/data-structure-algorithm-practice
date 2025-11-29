class Solution:
    def calculate(self, s: str) -> int:
        s = s.replace(" ", "")
        stack = []
        result = 0
        sign = 1
        operand = 0

        for idx, char in enumerate(s):
            if char.isdigit():
                operand = operand * 10 + int(char)
            if not char.isdigit() or idx == len(s) - 1:
                if char == "+":
                    result += operand * sign
                    sign = 1
                    operand = 0
                elif char == "-":
                    result += operand * sign
                    sign = -1
                    operand = 0
                elif char == "(":
                    stack.append(result)
                    stack.append(sign)
                    result = 0
                    sign = 1
                elif char == ")":
                    result += operand * sign
                    result *= stack.pop()
                    result += stack.pop()
                    operand = 0
                    sign = 1
        return result + operand * sign


if __name__ == "__main__":
    s = "(1+(4+5+2)-3)+(6+8) "
    print(f"The solution is {Solution().calculate(s)}")

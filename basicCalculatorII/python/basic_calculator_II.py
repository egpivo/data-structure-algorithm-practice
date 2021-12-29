class SolutionStack:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def calculate(self, s: str) -> int:
        s += "+"
        operators = ("+", "-", "*", "/")
        stack = []
        num = 0
        operator = ""
        for char in s:
            if char in operators:
                if operator == "-":
                    stack.append(-num)
                elif stack and operator == "/":
                    latest_num = stack.pop(-1)
                    stack.append(int(latest_num / num))
                elif stack and operator == "*":
                    latest_num = stack.pop(-1)
                    stack.append(latest_num * num)
                else:
                    stack.append(num)
                num = 0
                operator = char
            elif char.isdigit():
                num = num * 10 + int(char)
        return sum(stack)


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def calculate(self, s: str) -> int:
        current_num = last_num = 0
        result = 0
        s += "+"
        operator = "+"
        operators = ("+", "-", "*", "/")

        for char in s:
            if char in operators:
                if operator == "-":
                    result += last_num
                    last_num = -current_num
                elif operator == "+":
                    result += last_num
                    last_num = current_num
                elif operator == "*":
                    last_num += current_num
                elif operator == "/":
                    last_num = int(last_num / current_num)

                operator = char
                current_num = 0
            elif char.isdigit():
                current_num = current_num * 10 + int(char)

        result += last_num
        return result


if __name__ == "__main__":
    s = "14-3/2"
    print(f"The solution is {SolutionStack().calculate(s)}")
    print(f"The solution is {Solution().calculate(s)}")

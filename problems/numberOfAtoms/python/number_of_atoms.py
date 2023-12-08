import re
from collections import Counter


class Solution(object):
    def countOfAtoms(self, formula):
        parse = re.findall("([A-Z][a-z]*)(\d*)|(\()|(\))(\d*)", formula)
        stack = [Counter()]

        for atom, num1, opening_parenthis, closing_parenthis, num2 in parse:
            if atom:
                stack[-1][atom] += int(num1 or 1)
            if opening_parenthis:
                stack.append(Counter())
            if closing_parenthis:
                atom_pair = stack.pop()
                for key, value in atom_pair.items():
                    stack[-1][key] += value * int(num2 or 1)

        answer = "".join(
            [
                name + (str(stack[-1][name])) if stack[-1][name] > 1 else ""
                for name in sorted(stack[-1])
            ]
        )
        return answer


if __name__ == "__main__":
    formula = "K4(ON(SO3)2)2"
    print(Solution().countOfAtoms(formula))

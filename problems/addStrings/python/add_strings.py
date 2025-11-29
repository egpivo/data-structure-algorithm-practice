class Solution:
    """
    Complexity
    ----------
    - TC: O(max(p1, p2))
    - SC: O(1)
    """

    def addStrings(self, num1: str, num2: str) -> str:
        p1 = len(num1)
        p2 = len(num2)
        answer = ""
        carry = 0
        while p1 > 0 or p2 > 0:
            integer1 = self.stringTointeger(num1[p1 - 1]) if p1 > 0 else 0
            integer2 = self.stringTointeger(num2[p2 - 1]) if p2 > 0 else 0
            partial_sum = integer1 + integer2 + carry
            value = partial_sum % 10
            carry = partial_sum // 10
            answer = str(value) + answer
            p1 -= 1
            p2 -= 1

        return str(carry) + answer if carry > 0 else answer

    def stringTointeger(self, char: str) -> int:
        return ord(char) - ord("0")


if __name__ == "__main__":
    num1 = "456"
    num2 = "77"

    print(Solution().addStrings(num1, num2))

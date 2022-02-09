class Solution:
    """
    Complexity
    ----------
    - N: the length of a
    - M: the lenght of b
    - TC: O(N*M)
    - SC: O(1)
    """

    def addBinary(self, a: str, b: str) -> str:
        p1 = len(a)
        p2 = len(b)

        answer = ""
        carry = 0
        while p1 > 0 or p2 > 0:
            a_bin = self.stringToBinary(a[p1 - 1]) if p1 > 0 else 0
            b_bin = self.stringToBinary(b[p2 - 1]) if p2 > 0 else 0

            total = a_bin + b_bin + carry
            answer += str(total % 2)
            carry = total // 2

            p1 -= 1
            p2 -= 1
        if carry:
            answer += "1"
        return answer[::-1]

    def stringToBinary(self, string: str) -> int:
        return 1 if string == "1" else 0


if __name__ == "__main__":
    a = "1010"
    b = "1011"
    print(f"{Solution().addBinary(a, b)}")

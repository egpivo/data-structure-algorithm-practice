class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        if numerator == 0:
            return "0"

        sign = bool(numerator > 0) ^ bool(denominator > 0)
        numerator, denominator = abs(numerator), abs(denominator)
        result = ("-" if sign else "") + str(numerator // denominator)
        remainder = numerator % denominator

        if remainder == 0:
            return result

        result += "."
        pos = {}
        while remainder != 0:
            if not remainder in pos:
                pos[remainder] = len(result)
            else:
                return result[:pos[remainder]] + "(" + result[pos[remainder]:] + ")"

            result += str((remainder * 10) // denominator)
            remainder = (remainder * 10) % denominator
        return result


if __name__ == "__main__":
    numerator = 4
    denominator = 333
    print(f"Solution: {Solution().fractionToDecimal(numerator, denominator)}")

from typing import List


class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        result = []
        low_length = len(str(low))
        high_length = len(str(high))

        for digit_len in range(low_length, high_length + 1):
            for start_digit in range(1, 10 - digit_len + 1):
                num = 0
                for i in range(digit_len):
                    num = num * 10 + (start_digit + 1)
                if low <= num <= high:
                    result.append(num)
        return result


if __name__ == "__main__":
    low = 1000
    high = 13000
    print(Solution().sequentialDigits(low, high))

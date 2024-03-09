class Solution:
    """
    Complexity
    ----------
    - TC: O(log n)
    - SC: O(1)
    """

    def divide(self, dividend: int, divisor: int) -> int:
        # Constants for 32-bit integer limits
        INT_MAX = 2**31 - 1
        INT_MIN = -(2**31)

        # Check for division by zero
        if divisor == 0:
            return INT_MAX if dividend >= 0 else INT_MIN

        # Determine the sign of the result
        is_negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values for easier computation
        dividend, divisor = abs(dividend), abs(divisor)

        # Initialize result and power for bitwise division
        result = 0
        power = 31

        # Perform the division using bitwise operations
        while power >= 0:
            current_divisor = divisor << power
            if current_divisor <= dividend:
                # If the current divisor can be subtracted from the dividend
                # Add the corresponding power of 2 to the result
                result += 1 << power
                dividend -= current_divisor
            power -= 1

        # Apply the sign to the result
        result = -result if is_negative else result

        # Ensure the result is within the 32-bit signed integer range
        result = max(min(result, INT_MAX), INT_MIN)

        # Return the final result
        return result


if __name__ == "__main__":
    print(f"Solution: {Solution().divide(dividend=7, divisor=3)}")

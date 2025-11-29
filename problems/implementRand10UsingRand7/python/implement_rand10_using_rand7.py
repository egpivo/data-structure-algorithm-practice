# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


class Solution:
    def rand10(self):
        """
        Note
        ----
        - Rejection Sampling
        """
        index = acceptance = 40
        while index >= acceptance:
            row = rand7()
            col = rand7()
            index = (row - 1) * 7 + col - 1
        return (index % 10) + 1

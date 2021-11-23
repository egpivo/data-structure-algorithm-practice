# """
# This is BinaryMatrix's API interface.
# You should not implement it, or speculate about its implementation
# """
# class BinaryMatrix(object):
#    def get(self, row: int, col: int) -> int:
#    def dimensions(self) -> list[]:


class SolutionBS:
    """

    Complexity
    ----------
    - N: rows
    - M: cols
    - TC: O(NlogM)
    - SC: O(1)
    """
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimenstion()
        smallest_index = cols

        for row in rows:
            low = 0
            high = cols - 1
            while low < high:
                mid = low + (high - low) // 2
                if binaryMatrix.get(row, mid) == 0:
                    low = mid + 1
                else:
                    high = mid

            if binaryMatrix.get(row, low) == 1:
                smallest_index = min(smallest_index, low)

        return -1 if smallest_index == cols else smallest_index

class Solution:
    """

    Complexity
    ----------
    - N: rows
    - M: cols
    - TC: O(N+M)
    - SC: O(1)
    """
    def leftMostColumnWithOne(self, binaryMatrix: 'BinaryMatrix') -> int:
        rows, cols = binaryMatrix.dimenstion()
        current_row = 0
        current_col = cols -1

        while current_row < rows and current_col >= 0:
            if binaryMatrix.get(current_row, current_col) == 0:
                current_row += 1
            else:
                current_col -= 1

        return current_col + 1 if current_col != cols - 1 else -1

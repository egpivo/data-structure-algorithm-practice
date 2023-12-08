from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(mlogn)
    - SC: O(1)
    """

    def findPeakGrid(self, mat: List[List[int]]) -> List[int]:
        high_col, low_col = len(mat[0]) - 1, 0

        while low_col <= high_col:
            mid_col = low_col + (high_col - low_col) // 2

            max_row = 0
            for i in range(len(mat)):
                max_row = i if mat[i][mid_col] >= mat[max_row][mid_col] else max_row
            is_left_larger = (
                mid_col - 1 >= low_col
                and mat[max_row][mid_col] < mat[max_row][mid_col - 1]
            )
            is_right_larger = (
                mid_col + 1 <= high_col
                and mat[max_row][mid_col] < mat[max_row][mid_col + 1]
            )
            if not is_left_larger and not is_right_larger:
                return [max_row, mid_col]
            elif is_right_larger:
                low_col = mid_col + 1
            else:
                high_col = mid_col - 1

        return []


if __name__ == "__main__":
    mat = [[25, 37, 23, 37, 19], [45, 19, 2, 43, 26], [18, 1, 37, 44, 50]]
    print(f"{Solution().findPeakGrid(mat)}")

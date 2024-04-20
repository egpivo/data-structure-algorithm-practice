from typing import List


class Solution:
    """
    - Time complexity: O(mn)
    - Space complexity: O(mn)
    """

    def findFarmland(self, land: List[List[int]]) -> List[List[int]]:
        rows, cols = len(land), len(land[0])
        farmlands = []

        def dfs(row, col, max_row, max_col):
            # Base cases: out of bounds or not land
            if row >= rows or col >= cols or land[row][col] == 0:
                return max_row, max_col

            # Update bottom-right corner coordinates
            max_row = max(max_row, row)
            max_col = max(max_col, col)

            # Mark the land as visited
            land[row][col] = 0

            # Explore adjacent land cells
            max_row, max_col = dfs(row + 1, col, max_row, max_col)
            max_row, max_col = dfs(row, col + 1, max_row, max_col)
            return max_row, max_col

        # Iterate through all cells in the land
        for row in range(rows):
            for col in range(cols):
                # If current cell is land
                if land[row][col] == 1:
                    # Get top-left and bottom-right corners
                    top_left = (row, col)
                    bottom_right = dfs(row, col, row, col)
                    # Append farmland coordinates
                    farmlands.append([*top_left, *bottom_right])

        return farmlands


if __name__ == "__main__":
    land = [[1, 0, 0], [0, 1, 1], [0, 1, 1]]
    print(f"Solution: {Solution().findFarmland(land)}")

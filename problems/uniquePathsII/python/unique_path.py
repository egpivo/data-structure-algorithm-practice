from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time: O(mn)
    - Space: O(1) 
    """

    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        nrows = len(obstacleGrid)
        ncols = len(obstacleGrid[0])

        if obstacleGrid[0][0] == 1:
            return 0

        obstacleGrid[0][0] = 1

        for i in range(1, nrows):
            obstacleGrid[i][0] = int(obstacleGrid[i][0] == 0 and obstacleGrid[i-1][0] == 1)

        for j in range(1, ncols):
            obstacleGrid[0][j] = int(obstacleGrid[0][j] == 0 and obstacleGrid[0][j-1] == 1)

        for i in range(1, nrows):
            for j in range(1, ncols):
                if obstacleGrid[i][j] == 0:
                    obstacleGrid[i][j] = obstacleGrid[i-1][j] + obstacleGrid[i][j-1]
                else:
                    obstacleGrid[i][j] = 0

        return obstacleGrid[nrows-1][ncols-1]

if __name__ == "__main__":
    obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
    print(f"Solution: {Solution().uniquePathsWithObstacles(obstacleGrid)}")

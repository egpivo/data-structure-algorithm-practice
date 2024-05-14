## [Path with Maximum Gold](https://leetcode.com/problems/path-with-maximum-gold/description/)

In a gold mine grid of size m x n, each cell in this mine has an integer representing the amount of gold in that cell, 0 if it is empty.

Return the maximum amount of gold you can collect under the conditions:

- Every time you are located in a cell you will collect all the gold in that cell.
- From your position, you can walk one step to the left, right, up, or down.
- You can't visit the same cell more than once.
- Never visit a cell with 0 gold.
- You can start and stop collecting gold from any position in the grid that has some gold.


- Example:
```
Input: grid = [[0,6,0],[5,8,7],[0,9,0]]
Output: 24
```

- My solution: https://leetcode.com/problems/path-with-maximum-gold/solutions/5154628/backtracking-approach/

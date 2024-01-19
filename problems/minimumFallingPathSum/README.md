## [Minimum Falling Path Sum](https://leetcode.com/problems/minimum-falling-path-sum/)

Given an n x n array of integers matrix, return the minimum sum of any falling path through matrix.

A falling path starts at any element in the first row and chooses the element in the next row that is either directly below or diagonally left/right. Specifically, the next element from position (row, col) will be (row + 1, col - 1), (row + 1, col), or (row + 1, col + 1).


#### Example 1:
```
Input: matrix = [[2,1,3],[6,5,4],[7,8,9]]
Output: 13
```

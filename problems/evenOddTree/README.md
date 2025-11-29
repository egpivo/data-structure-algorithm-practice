## [Even Odd Tree](https://leetcode.com/problems/even-odd-tree/description/)

A binary tree is named Even-Odd if it meets the following conditions:

- The root of the binary tree is at level index 0, its children are at level index 1, their children are at level index 2, etc.
- For every even-indexed level, all nodes at the level have odd integer values in strictly increasing order (from left to right).
- For every odd-indexed level, all nodes at the level have even integer values in strictly decreasing order (from left to right).
Given the root of a binary tree, return true if the binary tree is Even-Odd, otherwise return false.


- Example 1:
```
Input: root = [1,10,4,3,null,7,9,12,8,6,null,null,2]
Output: true
```

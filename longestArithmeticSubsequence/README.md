## [Longest Arithmetic Subsequence](https://leetcode.com/problems/longest-arithmetic-subsequence/)

Given an array `nums` of integers, return the length of the longest arithmetic subsequence in `nums`.

Recall that a subsequence of an array nums is a list `nums[i1], nums[i2], ..., nums[ik]` with `0 <= i1 < i2 < ... < ik <= nums.length - 1`, and that a sequence seq is arithmetic if `seq[i+1]` - `seq[i]` are all the same value (for `0 <= i < seq.length - 1`). 
- Example:
```
Input: root = [1,2,3,4,5,6]
Output: true
Explanation: Every level before the last is full (i.e., levels with node-values `{1}` and `{2, 3}`), and all nodes in the last level `({4, 5, 6})` are as far left as possible.
```

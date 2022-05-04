## [Maximum Difference Between Node and Ancestor](https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/)

Given the `root` of a binary tree, find the maximum value `v` for which there exist different nodes `a` and `b` where `v = |a.val - b.val|` and `a` is an ancestor of `b`.

A node `a` is an ancestor of `b` if either: any child of `a` is equal to `b` or any child of `a` is an ancestor of `b`.

- Example:
```
Input: root = [1,null,2,null,0,3]
    1
     \
      2
       \
        0
       /
      3

Output: 3
```
## [Smallest String Starting From Leaf](https://leetcode.com/problems/smallest-string-starting-from-leaf/description/)

You are given the root of a binary tree where each node has a value in the range [0, 25] representing the letters 'a' to 'z'.

Return the lexicographically smallest string that starts at a leaf of this tree and ends at the root.

As a reminder, any shorter prefix of a string is lexicographically smaller.

- For example, "ab" is lexicographically smaller than "aba".
A leaf of a node is a node that has no children.


- Example:
```
Input: root = [0,1,2,3,4,3,4]
Output: "dba"
```

- My solution: https://leetcode.com/problems/smallest-string-starting-from-leaf/solutions/5024886/dfs-approach/

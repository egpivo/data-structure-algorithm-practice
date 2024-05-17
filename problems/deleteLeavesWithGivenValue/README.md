## [Delete Leaves With a Given Value](https://leetcode.com/problems/delete-leaves-with-a-given-value/description)

Given a binary tree root and an integer target, delete all the leaf nodes with value target.

Note that once you delete a leaf node with value target, if its parent node becomes a leaf node and has the value target, it should also be deleted (you need to continue doing that until you cannot).


- Example
```
Input: root = [1,2,3,2,null,2,4], target = 2
Output: [1,null,3,null,4]
```

- My solution: https://leetcode.com/problems/delete-leaves-with-a-given-value/solutions/5167767/postorder-traversal-approach/

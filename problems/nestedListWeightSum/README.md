## [Nested List Weight Sum](https://leetcode.com/problems/nested-list-weight-sum/)
You are given a nested list of integers `nestedList`. Each element is either an integer or a list whose elements may also be integers or other lists.

The `depth` of an integer is the number of lists that it is inside of. For example, the nested list `[1,[2,2],[[3],2],1]` has each integer's value set to its **depth**.

Return the sum of each integer in `nestedList` multiplied by its **depth**.

```
Input: nestedList = [[1,1],2,[1,1]]
Output: 10
Explanation: Four 1's at depth 2, one 2 at depth 1. 1*2 + 1*2 + 2*1 + 1*2 + 1*2 = 10.
```

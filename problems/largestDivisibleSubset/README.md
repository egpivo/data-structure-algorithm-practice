## [Base 7](https://leetcode.com/problems/base-7/)

Given a set of distinct positive integers nums, return the largest subset answer such that every pair `(answer[i], answer[j])` of elements in this subset satisfies:

- `answer[i] % answer[j] == 0`, or
- `answer[j] % answer[i] == 0`
If there are multiple solutions, return any of them.

- Example:
```
Input: nums = [1,2,4,8]
Output: [1,2,4,8]
```

## [Cut Wood](https://leetcode.com/discuss/interview-question/354854/facebook-phone-screen-cut-wood)

Given n pieces of wood with length `L[i]` (integer array).
Cut them into small pieces to guarantee you could have equal or more than `k` pieces with the same length. What is the longest length you can get from the n pieces of wood?Given `L` & k, return the maximum length of the small pieces.

- Example 1:
```
Input: wood = [5, 9, 7], k = 4
Output: 4
Explanation:
5 -> 4 + 1
9 -> 4 * 2 + 1
7 -> 4 + 3
```

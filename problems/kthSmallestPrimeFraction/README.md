## [K-th Smallest Prime Fraction](https://leetcode.com/problems/k-th-smallest-prime-fraction/description/)

You are given a sorted integer array arr containing 1 and prime numbers, where all the integers of arr are unique. You are also given an integer k.

For every i and j where `0 <= i < j < arr.length`, we consider the fraction `arr[i] / arr[j]`.

Return the kth smallest fraction considered. Return your answer as an array of integers of size 2, where `answer[0] == arr[i]` and `answer[1] == arr[j]`.



- Example:
```
Input: arr = [1,2,3,5], k = 3
Output: [2,5]
```

- My solution: https://leetcode.com/problems/k-th-smallest-prime-fraction/solutions/5137564/min-heap-approach/

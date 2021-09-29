## [The Earliest Moment When Everyone Become Friends](https://leetcode.com/problems/the-earliest-moment-when-everyone-become-friends/)

There are `n` people in a social group labeled from `0` to `n - 1`. You are given an array logs where `logs[i] = [timestampi, xi, yi]` indicates that `xi` and `yi` will be friends at the time timestampi.

Friendship is symmetric. That means if `a` is friends with `b`, then `b` is friends with `a`. Also, person `a` is acquainted with a person `b` if `a` is friends with `b`, or `a` is a friend of someone acquainted with `b`.

Return the earliest time for which every person became acquainted with every other person. If there is no such earliest time, return `-1`.

`
Input: logs = [[0,2,0],[1,0,1],[3,0,3],[4,1,2],[7,3,1]], n = 4
Output: 3
```

## [Friends Of Appropriate Ages](https://leetcode.com/problems/friends-of-appropriate-ages/description/)
There are n persons on a social media website. You are given an integer array ages where ages[i] is the age of the ith person.

A Person x will not send a friend request to a person y (x != y) if any of the following conditions is true:

- `age[y] <= 0.5 * age[x] + 7`
- `age[y] > age[x]`
- `age[y] > 100 && age[x] < 100`
Otherwise, x will send a friend request to `y`.

Note that if x sends a request to y, y will not necessarily send a request to x. Also, a person will not send a friend request to themself.

Return the total number of friend requests made.


- Example 1:
```
Input: ages = [20,30,100,110,120]
Output: 3
```

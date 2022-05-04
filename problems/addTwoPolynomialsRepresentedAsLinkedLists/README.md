## [Add Two Polynomials Represented as Linked Lists](https://leetcode.com/problems/add-two-polynomials-represented-as-linked-lists/)

A polynomial linked list is a special type of linked list where every node represents a term in a polynomial expression.

Each node has three attributes:

- `coefficient`: an integer representing the number multiplier of the term. The coefficient of the term 9x4 is 9.
- `power`: an integer representing the exponent. The power of the term 9x4 is 4.
- `next`: a pointer to the next node in the list, or null if it is the last node of the list.

Example:
```
Input: poly1 = [[1,1]], poly2 = [[1,0]]
Output: [[1,1],[1,0]]
Explanation: poly1 = x. poly2 = 1. The sum is x + 1.
```

## Note
1. Solution 1: Traverse an array with a hashtable/map stroing key-value pais of an element and the corresponding count
    - Time complexity: O(N) or O(NlogN) 
        - Traverse an array: O(N)
        - Insert an element to a hashtable `unordered_map`: O(1)
        - Insert an element to a map `map`: O(logN)
    - Space complexity: O(N)

2. Solution 2: Save a traversing element into a hashtable if the element does not exist in the hashtable. Otherwise, remove it.
    - Time complexity: O(N)
    - Space Complexity: <= O(N)
    - Insert an element to `unordered_set`
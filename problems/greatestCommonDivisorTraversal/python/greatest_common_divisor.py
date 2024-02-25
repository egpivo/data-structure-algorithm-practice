from collections import defaultdict, deque
from math import ceil, sqrt
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(max_num * log(log(max_num))
    - SC: O(max_num + edge)
    """

    def canTraverseAllPairs(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        if 1 in nums:
            return False

        max_num = max(nums) + 1
        sieve = self.buildSieve(max_num)
        graph = self.buildGraph(nums, sieve)
        return self.isConnected(graph, nums)

    def buildSieve(self, max_num: int) -> List[int]:
        # Sieve of Eratosthenes to find prime factors
        sieve = list(range(max_num))

        for i in range(4, max_num, 2):
            sieve[i] = 2

        # this part of the code marks non-prime multiples of prime numbers,
        # in order to store the smallest prime factor of each non-prime number.
        for i in range(3, ceil(sqrt(max_num))):
            if sieve[i] == i:
                for j in range(i * i, max_num, i):
                    if sieve[j] == j:
                        sieve[j] = i

        return sieve

    def buildGraph(self, nums: List[int], sieve: List[int]) -> defaultdict:
        graph = defaultdict(set)

        def factorize(num):
            while num != 1:
                yield sieve[num]
                num //= sieve[num]

        for num in set(nums):
            for prime_factor in factorize(num):
                graph[num].add(prime_factor)
                graph[prime_factor].add(num)

        return graph

    def isConnected(self, graph: defaultdict, nums: List[int]) -> bool:
        # BFS traversal to check if all numbers are connected
        queue, seen = deque([nums[0]]), {nums[0]}

        while queue:
            current_num = queue.popleft()
            for neighbor in graph[current_num]:
                if neighbor not in seen:
                    seen.add(neighbor)
                    queue.append(neighbor)

        return len(seen) == len(graph)

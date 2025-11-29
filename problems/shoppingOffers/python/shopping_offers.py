from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(k^n)$
        - $n$ is the number of items.
        - $k$:is the number of special offers
    - Space complexity: $O(n)$
    """

    def shoppingOffers(
        self, price: List[int], special: List[List[int]], needs: List[int]
    ) -> int:
        n = len(price)

        def can_apply_offer(offer, needs):
            for i in range(n):
                if offer[i] > needs[i]:
                    return False
            return True

        def apply_offer(offer, needs):
            for i in range(n):
                needs[i] -= offer[i]

        visited = {}

        def backtrack(needs):
            if tuple(needs) in visited:
                return visited[tuple(needs)]

            min_cost = sum(p * need for p, need in zip(price, needs))
            for spe in special:
                if can_apply_offer(spe[:-1], needs):
                    apply_offer(spe[:-1], needs)
                    min_cost = min(min_cost, backtrack(needs) + spe[-1])
                    apply_offer([-x for x in spe[:-1]], needs)
            visited[tuple(needs)] = min_cost
            return min_cost

        return backtrack(needs)


if __name__ == "__main__":
    price = [2, 5]
    special = [[3, 0, 5], [1, 2, 10]]
    needs = [3, 2]

    print(Solution().shoppingOffers(price, special, needs))

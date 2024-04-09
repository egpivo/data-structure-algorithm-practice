from typing import List


class Solution1:
    """
    Complexity
    ----------
    - TC: O(sum(tickets))
    - SC: O(1)
    """

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        n = len(tickets)
        total_time = 0
        current_person = 0

        while tickets[k] != 0:
            if tickets[current_person] > 0:
                tickets[current_person] -= 1
                total_time += 1

            current_person = (current_person + 1) % n

        return total_time


class Solution2:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """

    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        len(tickets)
        total_time = 0

        for person, ticket in enumerate(tickets):
            if person <= k:
                total_time += min(ticket, tickets[k])
            else:
                total_time += min(ticket, tickets[k] - 1)

        return total_time


if __name__ == "__main__":
    tickets = [2, 3, 2]
    k = 2

    print(f"The solution1 is {Solution1().timeRequiredToBuy(tickets, k)}")
    tickets = [2, 3, 2]
    k = 2
    print(f"The solution2 is {Solution2().timeRequiredToBuy(tickets, k)}")

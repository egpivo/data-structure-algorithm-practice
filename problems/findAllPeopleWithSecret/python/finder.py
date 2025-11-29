from collections import defaultdict, deque
from itertools import groupby
from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(E+V)
    - SC: O(V)
    """

    def findAllPeople(
        self, n: int, meetings: List[List[int]], firstPerson: int
    ) -> List[int]:
        # Initialize the set of people who know the secret
        secret_knowers = {0, firstPerson}
        # Group meetings by time
        meetings_by_time = groupby(
            sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]
        )

        # Iterate through meetings grouped by time
        for _, grouped_meetings in meetings_by_time:
            # Initialize a set for the current time's meeting participants
            current_time_participants = set()
            # Create a graph to represent connections between participants
            graph = defaultdict(list)

            # Process each meeting in the current time group
            for person1, person2, _ in grouped_meetings:
                graph[person1].append(person2)
                graph[person2].append(person1)

                # Add participants to the queue if they already know the secret
                if person1 in secret_knowers or person2 in secret_knowers:
                    current_time_participants.add(person1)
                    current_time_participants.add(person2)

            # Use a deque for efficient queue operations
            queue = deque(current_time_participants)
            # Explore the connections to find new people who know the secret
            while queue:
                current_person = queue.popleft()
                for connected_person in graph[current_person]:
                    if connected_person not in secret_knowers:
                        # Add the newly discovered person to the set and the queue
                        secret_knowers.add(connected_person)
                        queue.append(connected_person)

        # Convert the set of secret knowers to a list before returning
        return list(secret_knowers)


if __name__ == "__main__":
    n = 4
    flights = [[0, 1, 100], [1, 2, 100], [2, 0, 100], [1, 3, 600], [2, 3, 200]]
    src = 0
    dst = 3
    k = 1
    print(f"The solution is {Solution().findCheapestPrice(n, flights, src, dst, k)}")

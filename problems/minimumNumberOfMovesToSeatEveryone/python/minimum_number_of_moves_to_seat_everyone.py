from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n\log n)
    - SC: O(1)
    """

    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats.sort()
        students.sort()
        return sum(abs(seat - student) for seat, student in zip(seats, students))


if __name__ == "__main__":
    seats = [3, 1, 5]
    students = [2, 7, 4]
    print(Solution().minMovesToSeat(seats, students))

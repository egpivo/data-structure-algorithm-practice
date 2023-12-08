import heapq
from collections import Counter, defaultdict
from typing import List


class SolutionHashMap:
    """

    Complexity
    ----------
    TC: O(M * N * log(N * M))
    SC: O(N * M)
    """

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        nrow = len(mat)
        ncol = len(mat[0])

        diagnoals = defaultdict(list)
        for row in range(nrow):
            for col in range(ncol):
                diagnoals[row - col].append(mat[row][col])

        for diagnoal in diagnoals.values():
            heapq.heapify(diagnoal)

        for row in range(nrow):
            for col in range(ncol):
                mat[row][col] = heapq.heappop(diagnoals[row - col])

        return mat


class SolutionOneByOne:
    """

    Complexity
    ----------
    TC: O(M * N * log(N * M))
    SC: O(min(N, M))
    """

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        nrow = len(mat)
        ncol = len(mat[0])

        for row in range(nrow):
            self.sort_diagonal(mat, row, 0)

        for col in range(1, ncol):
            self.sort_diagonal(mat, 0, col)

        return mat

    def sort_diagonal(self, mat, row, col):
        nrow = len(mat)
        ncol = len(mat[0])
        diagonals = []
        diagonal_length = min(nrow - row, ncol - col)
        for i in range(diagonal_length):
            diagonals.append(mat[row + i][col + i])

        heapq.heapify(diagonals)

        for i in range(diagonal_length):
            mat[row + i][col + i] = heapq.heappop(diagonals)


class SolutionCountingSort:
    """

    Complexity
    ----------
    TC: O(M * N)
    SC: O(min(N, M))
    """

    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        nrow = len(mat)
        ncol = len(mat[0])

        for row in range(nrow):
            self.sort_diagonal(mat, row, 0)

        for col in range(1, ncol):
            self.sort_diagonal(mat, 0, col)

        return mat

    def sort_diagonal(self, mat, row, col):
        nrow = len(mat)
        ncol = len(mat[0])
        diagonals = []
        diagonal_length = min(nrow - row, ncol - col)
        for i in range(diagonal_length):
            diagonals.append(mat[row + i][col + i])

        diagonals = self.counting_sort(diagonals)

        for i in range(diagonal_length):
            mat[row + i][col + i] = heapq.heappop(diagonals)

    def counting_sort(self, nums):
        # Assume nums in [0, 100]
        minimum, maximum = 0, 100
        sorted_nums = []

        counts = Counter(nums)
        for i in range(minimum, maximum + 1):
            sorted_nums.extend([i] * counts[i])
        return sorted_nums


if __name__ == "__main__":
    mat = [[3, 3, 1, 1], [2, 2, 1, 2], [1, 1, 1, 2]]
    print(SolutionHashMap().diagonalSort(mat))
    print(SolutionOneByOne().diagonalSort(mat))
    print(SolutionCountingSort().diagonalSort(mat))

from typing import List


class Solution1:
    """
    Complexity
    ----------
    - SC: O(m\log m)
    - TC: O(m)
    """

    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        m, n = len(score), len(score[0])

        # Create a list of tuples with the k-th column values and corresponding row indices
        k_col = [(score[i][k], i) for i in range(m)]

        # Sort the list in descending order based on the k-th column values
        k_col.sort(reverse=True)

        # Create the result list using the sorted row indices
        result = [score[index] for _, index in k_col]

        return result


class Solution2:
    """
    Complexity
    ----------
    - SC: O(m\log m)
    - TC: O(1)
    """

    def sortTheStudents(self, scores: List[List[int]], k: int) -> List[List[int]]:
        return sorted(scores, key=lambda x: x[k], reverse=True)


if __name__ == "__main__":
    score = [[10, 6, 9, 1], [7, 5, 11, 2], [4, 8, 3, 15]]
    k = 2
    print(f"Solution: {Solution1().sortTheStudents(score, k)}")
    print(f"Solution: {Solution2().sortTheStudents(score, k)}")

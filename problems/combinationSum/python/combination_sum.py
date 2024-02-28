from typing import List


class BackTrackingSolution:
    """Backtracking

    Complexity
    ----------
    - TC: O(n^(target/min(candidates)))
       - n = len(candidates)
    - SC: O(target/min(candidates))
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        answer = []
        n = len(candidates)

        def dfs(collection, idx):
            if sum(collection) > target:
                return
            elif sum(collection) == target:
                answer.append(collection)
                return

            for i in range(idx, n):
                dfs(collection + [candidates[i]], i)

        dfs([], 0)
        return answer


class DpSolution:
    """Dynamic Programming

    Complexity
    ----------
    - TC: O(target ^ 2 * n))
       - n = len(candidates)
    - SC: O(target ^ 2))
    """

    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        dp = [[] for _ in range(target + 1)]

        for candidate in candidates:
            for c in range(candidate, target + 1):
                if candidate == c:
                    dp[c].append([candidate])

                for cumulative in dp[c - candidate]:
                    dp[c].append(cumulative + [candidate])
        print(dp)
        return dp[-1]


if __name__ == "__main__":
    candidates = [2, 3, 6, 7]
    target = 7

    print(f"Solution: {BackTrackingSolution().combinationSum(candidates, target)}")
    print(f"Solution: {DpSolution().combinationSum(candidates, target)}")

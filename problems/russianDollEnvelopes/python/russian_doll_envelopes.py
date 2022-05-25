from bisect import bisect_left
from typing import List


class Solution:
    
    """
    Complexity
    ----------
    - Time: O(nlog(n))
    - Space: O(n)
    """

    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))

        # longest increasing subsequence algorithm
        def lis(nums):
            dp = []

            for num in nums:
                idx = bisect_left(dp, num)
                if idx == len(dp):
                    dp.append(num)
                else:
                    dp[idx] = num
            return len(dp)
        return lis([envelope[1] for envelope in envelopes])


if __name__ == "__main__":
    envelopes = [[5,4],[6,4],[6,7],[2,3]]
    print(f"Solution: {Solution().maxEnvelopes(envelopes)}")

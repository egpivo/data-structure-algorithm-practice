from collections import Counter


class Solution:
    def minDeletions(self, s: str) -> int:

        """
        Complexity
        ----------
        TC: O(nlog(n))
        SC: O(n)
        """
        counter = Counter(s)
        count_list = sorted(counter.values(), reverse=True)

        deleted, tracker = 0, []

        for num in count_list:
            if not num in tracker:
                tracker.append(num)
                continue
            while tracker and num in tracker:
                deleted += 1
                num -= 1
            tracker.append(num)

        return deleted


if __name__ == "__main__":
    s = "aaabbbcc"
    print(f"Solution: {Solution().minDeletions(s)}")

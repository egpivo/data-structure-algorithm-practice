from collections import Counter


class Solution:
    def minSteps(self, s: str, t: str) -> int:
        source_counts = Counter(s)
        target_counts = Counter(t)
        steps_needed = 0

        for char, source_freq in source_counts.items():
            if target_counts[char] < source_freq:
                steps_needed += source_freq - target_counts[char]
                target_counts[char] = source_freq

        return steps_needed


if __name__ == "__main__":
    print(f"Solution: {Solution().minSteps('aba', 'bab')}")

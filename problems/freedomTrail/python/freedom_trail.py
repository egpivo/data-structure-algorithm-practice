from collections import defaultdict


class Solution:
    """
    Complexity
    ----------
    - TC: O(mn^2)
    - SC: O(mn)
    - m: length of key
    - n: length of right
    """

    def findRotateSteps(self, ring: str, key: str) -> int:
        ring_indices = defaultdict(
            list
        )  # Dictionary to store indices of each character in the ring

        # Populate the ring_indices dictionary
        for i, char in enumerate(ring):
            ring_indices[char].append(i)

        # Define a memoization dictionary to store computed results
        memo = {}

        # Define a helper function to find the minimum steps using dynamic programming
        def dp(i, j):
            # If all characters of the key are processed, return 0
            if i == len(key):
                return 0

            # If the result is already memoized, return it
            if (i, j) in memo:
                return memo[(i, j)]

            # Calculate the minimum steps to align the ith character of the key with the jth character of the ring
            result = float("inf")
            for k in ring_indices[key[i]]:
                steps_to_rotate = abs(
                    j - k
                )  # Steps required to rotate the ring to align character k with character j
                steps = (
                    min(steps_to_rotate, len(ring) - steps_to_rotate) + 1
                )  # Press the button once to select the character
                steps += dp(
                    i + 1, k
                )  # Recursively calculate steps for the remaining characters
                result = min(result, steps)

            # Memoize the result
            memo[(i, j)] = result
            return result

        # Start the dynamic programming process with the first character of the key aligned with the first character of the ring
        return dp(0, 0)


if __name__ == "__main__":
    ring = "godding"
    key = "gd"
    print(f"The solution is {Solution().findRotateSteps(ring, key)}")

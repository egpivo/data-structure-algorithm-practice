class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """

    def equalSubstring(self, s: str, t: str, max_cost: int) -> int:
        n = len(s)

        # Calculate the distance between corresponding characters
        distance = [abs(ord(s[i]) - ord(t[i])) for i in range(n)]
        max_length = 0
        current_cost = 0
        left = 0

        # Use a sliding window to find the maximum length substring
        for right in range(n):
            current_cost += distance[right]

            # If the current cost exceeds maxCost, shrink the window from the left
            while current_cost > max_cost:
                current_cost -= distance[left]
                left += 1

            # Update the maximum length
            max_length = max(max_length, right - left + 1)

        return max_length


if __name__ == "__main__":
    s = "abcd"
    t = "bcdf"
    max_cost = 3
    print(f"The solution is {Solution().equalSubstring(s, t, max_cost)}")

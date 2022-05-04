class Solution:
    def maximumSwap(self, num: int) -> int:

        """
        Complexity
        ----------
        TC: O(n)
        SC: O(1)
        """
        num_str = list(str(num))

        i = 0
        while i < len(num_str) - 1 and num_str[i] >= num_str[i + 1]:
            i += 1

        k = i
        for idx in range(len(num_str) - 1, i, -1):
            if num_str[idx] > num_str[k]:
                k = idx

        for idx in range(i + 1):
            if num_str[idx] < num_str[k]:
                break

        num_str[idx], num_str[k] = num_str[k], num_str[idx]

        return int("".join(num_str))


if __name__ == "__main__":
    num = 2736
    print(f"Solution: {Solution().maximumSwap(num)}")

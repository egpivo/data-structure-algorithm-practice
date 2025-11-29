from collections import Counter


class Solution:
    def customSortString(self, order: str, s: str) -> str:
        """
        Complexity
        ----------
        - TC: O(len(order) + len(s))
        - SC: O(len(s))
        """
        s_freq = Counter(s)

        ans = []
        for char in order:
            ans.append(char * s_freq[char])
            s_freq[char] = 0

        for key, val in s_freq.items():
            ans.append(key * val)

        return "".join(ans)


class SolutionII:
    def customSortString(self, order: str, s: str) -> str:
        """
        Complexity
        ----------
        - TC: O(len(order) + len(s))
        - SC: O(len(order) + len(s))
        """
        order_index_dict = {char: index for index, char in enumerate(order)}
        in_order_list = []
        out_order_list = []

        for char in s:
            if char in order_index_dict:
                in_order_list.append(char)
            else:
                out_order_list.append(char)

        return "".join(
            sorted(in_order_list, key=lambda x: order_index_dict.get(x))
            + out_order_list
        )


class SolutionIII:
    def customSortString(self, order: str, s: str) -> str:
        """
        Complexity
        ----------
        - TC: O(len(order) + len(s))
        - SC: O(len(order) + len(s))
        """
        order_freq_map = {char: 0 for char in order}
        remaining_list = []
        for char in s:
            if char in order_freq_map:
                order_freq_map[char] += 1
            else:
                remaining_list.append(char)
        ordered_str = ""
        for key, val in order_freq_map.items():
            ordered_str += key * val
        return ordered_str + "".join(remaining_list)


if __name__ == "__main__":
    order = "cba"
    s = "abcd"
    print(f"Solution: {Solution().customSortString(order, s)}")
    print(f"Solution: {SolutionII().customSortString(order, s)}")
    print(f"Solution: {SolutionIII().customSortString(order, s)}")

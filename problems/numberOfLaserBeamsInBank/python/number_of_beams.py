from typing import List


class Solution:
    """
    Complexity
    ----------
    - Time complexity: $O(m^3 \cdot n)$
        - $m$ is the number of rows
        - $n$ is the number of columns.
    - Space complexity: $O(1)$
    """

    def numberOfBeams(self, bank: List[str]) -> int:
        count = 0

        m = len(bank)
        len(bank[0])

        for r1 in range(m):
            devices_r1 = bank[r1].count("1")
            if devices_r1 == 0:
                continue
            for r2 in range(r1 + 1, m):
                devices_r2 = bank[r2].count("1")
                if devices_r2 == 0:
                    continue
                has_device_between = False
                for i in range(r1 + 1, r2):
                    if "1" in bank[i]:
                        has_device_between = True
                        break
                if not has_device_between:
                    count += devices_r1 * devices_r2
        return count


class Solution2:
    """
    Complexity
    ----------
    - Time complexity: $O(m \codt n)$
        - $m$ is the number of rows
        - $n$ is the number of columns.
    - Space complexity: $O(m)$
    """

    def numberOfBeams(self, bank: List[str]) -> int:
        beams = [b.count("1") for b in bank if "1" in b]
        return sum(previous * current for previous, current in zip(beams, beams[1:]))


if __name__ == "__main__":
    g = ["011001", "000000", "010100", "001000"]
    print(f"The Solution is {Solution().numberOfBeams(g)}")
    print(f"The Solution is {Solution2().numberOfBeams(g)}")

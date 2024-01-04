from typing import List


class Solution:
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


if __name__ == "__main__":
    g = ["011001", "000000", "010100", "001000"]
    print(f"The Solution is {Solution().numberOfBeams(g)}")

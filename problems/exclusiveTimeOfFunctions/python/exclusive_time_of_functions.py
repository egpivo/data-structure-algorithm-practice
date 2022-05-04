from typing import List


class Solution:
    def exclusiveTime(self, n: int, logs: List[str]) -> List[int]:
        stack = []
        durations = [0] * n
        prev = 0
        for log in logs:
            fid, indicator, ftime = log.split(":")
            fid, ftime = int(fid), int(ftime)
            if indicator == "start":
                if stack:
                    durations[stack[-1]] += ftime - prev
                stack.append(fid)
                prev = ftime
            else:
                durations[stack.pop()] += ftime - prev + 1
                prev = ftime + 1

        return durations


if __name__ == "__main__":
    n = 2
    logs = ["0:start:0", "1:start:2", "1:end:5", "0:end:6"]
    print(f"{Solution().exclusiveTime(n, logs)}")

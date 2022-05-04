class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s) != len(goal):
            return False

        if s == goal:
            seen = set()
            for char in s:
                if char in seen:
                    return True
                seen.add(char)
            return False

        pairs = []
        for char1, char2 in zip(s, goal):
            if char1 != char2:
                pairs.append([char1, char2])
            if len(pairs) >= 3:
                return False

        return len(pairs) == 2 and pairs[0] == pairs[1][::-1]


if __name__ == "__main__":
    s = "aaaaaaabc"
    goal = "aaaaaaacb"
    print(Solution().buddyStrings(s, goal))

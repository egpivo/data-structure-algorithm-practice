class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set("aeiouAEIOU")
        mid = len(s) // 2

        return sum(char in vowels for char in s[:mid]) == sum(
            char in vowels for char in s[mid:]
        )


if __name__ == "__main__":
    print(f"Solution: {Solution().halvesAreAlike('textbook')}")

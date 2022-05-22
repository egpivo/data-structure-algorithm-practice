class Solution:
    """
    Complexity
    ----------
    - Time: O(N^3)
    - Space: O(1) 
    """

    def countSubstrings(self, s: str) -> int:
        answer = 0
 
        for left in range(len(s)):
            right = len(s) - 1
            while left <= right:
                if self.is_palindromic(s, left, right):
                    answer += 1
                right -= 1
        
        return answer


    def is_palindromic(self, s: str, left: int, right: int) -> bool:
        while left < right:
            if s[left] != s[right]:
                return False
            left += 1
            right -= 1

        return True            


if __name__ == "__main__":
    s = "aaa"
    print(f"Solution: {Solution().countSubstrings(s)}")

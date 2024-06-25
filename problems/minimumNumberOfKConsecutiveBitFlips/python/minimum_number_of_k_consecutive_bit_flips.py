from typing import List


class Solution:
    """
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """
    def minKBitFlips(self, nums: List[int], k: int) -> int:
        n = len(nums)
        flip_count = 0
        flip = 0
        is_flipped = [0] * n

        for i in range(n):
            # If the flip effect goes out of bounds, revert the flip effect
            if i >= k:
                flip ^= is_flipped[i - k]

            # Determine if we need to flip starting from index i
            if nums[i] ^ flip == 0:
                if i + k > n:
                    return -1
                flip ^= 1
                is_flipped[i] = 1
                flip_count += 1

        return flip_count


if __name__ == "__main__":
    nums = [0,1,0]
    k = 1
    print(f"The solution is {Solution().minKBitFlips(nums, k)}")

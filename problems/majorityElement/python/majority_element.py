from collections import Counter
from typing import List


class Solution:
    """
    Brute force approach - inefficient.
    Complexity
    ----------
    - TC: O(n²)
    - SC: O(n)
    """
    def majorityElement(self, nums: List[int]) -> int:
        for i in set(nums):
            if nums.count(i) > len(nums) / 2:
                return i
        return -1


class SolutionBoyerMoore:
    """
    Boyer-Moore Voting Algorithm - optimal solution.
    Complexity
    ----------
    - TC: O(n)
    - SC: O(1)
    """
    def majorityElement(self, nums: List[int]) -> int:
        count = 0
        candidate = None
        
        # Phase 1: Find a candidate
        for num in nums:
            if count == 0:
                candidate = num
            count += 1 if num == candidate else -1
        
        # Phase 2: Verify candidate (optional, but good practice)
        # Since problem guarantees majority exists, we can skip verification
        return candidate


class SolutionCounter:
    """
    Using Counter - simple and readable.
    Complexity
    ----------
    - TC: O(n)
    - SC: O(n)
    """
    def majorityElement(self, nums: List[int]) -> int:
        freq = Counter(nums)
        return freq.most_common(1)[0][0]


class SolutionSort:
    """
    Using sorting - majority element will be at middle position.
    Complexity
    ----------
    - TC: O(n log n)
    - SC: O(1) or O(n) depending on sort implementation
    """
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        return nums[len(nums) // 2]


if __name__ == "__main__":
    # Test case 1: Standard case
    nums1 = [2, 2, 1, 1, 1, 2, 2]
    result1a = Solution().majorityElement(nums1)
    result1b = SolutionBoyerMoore().majorityElement(nums1)
    result1c = SolutionCounter().majorityElement(nums1)
    result1d = SolutionSort().majorityElement(nums1)
    print(f"Test 1: {result1a}, {result1b}, {result1c}, {result1d} (Expected: 2)")
    assert result1a == 2, "Test 1a failed"
    assert result1b == 2, "Test 1b failed"
    assert result1c == 2, "Test 1c failed"
    assert result1d == 2, "Test 1d failed"
    
    # Test case 2: Single element
    nums2 = [1]
    result2a = Solution().majorityElement(nums2)
    result2b = SolutionBoyerMoore().majorityElement(nums2)
    result2c = SolutionCounter().majorityElement(nums2)
    result2d = SolutionSort().majorityElement(nums2)
    print(f"Test 2: {result2a}, {result2b}, {result2c}, {result2d} (Expected: 1)")
    assert result2a == 1, "Test 2a failed"
    assert result2b == 1, "Test 2b failed"
    assert result2c == 1, "Test 2c failed"
    assert result2d == 1, "Test 2d failed"
    
    # Test case 3: All same elements
    nums3 = [3, 3, 3, 3]
    result3a = Solution().majorityElement(nums3)
    result3b = SolutionBoyerMoore().majorityElement(nums3)
    result3c = SolutionCounter().majorityElement(nums3)
    result3d = SolutionSort().majorityElement(nums3)
    print(f"Test 3: {result3a}, {result3b}, {result3c}, {result3d} (Expected: 3)")
    assert result3a == 3, "Test 3a failed"
    assert result3b == 3, "Test 3b failed"
    assert result3c == 3, "Test 3c failed"
    assert result3d == 3, "Test 3d failed"
    
    # Test case 4: Another standard case
    nums4 = [3, 2, 3]
    result4a = Solution().majorityElement(nums4)
    result4b = SolutionBoyerMoore().majorityElement(nums4)
    result4c = SolutionCounter().majorityElement(nums4)
    result4d = SolutionSort().majorityElement(nums4)
    print(f"Test 4: {result4a}, {result4b}, {result4c}, {result4d} (Expected: 3)")
    assert result4a == 3, "Test 4a failed"
    assert result4b == 3, "Test 4b failed"
    assert result4c == 3, "Test 4c failed"
    assert result4d == 3, "Test 4d failed"
    
    # Test case 5: Large array
    nums5 = [1] * 5 + [2] * 3
    result5a = Solution().majorityElement(nums5)
    result5b = SolutionBoyerMoore().majorityElement(nums5)
    result5c = SolutionCounter().majorityElement(nums5)
    result5d = SolutionSort().majorityElement(nums5)
    print(f"Test 5: {result5a}, {result5b}, {result5c}, {result5d} (Expected: 1)")
    assert result5a == 1, "Test 5a failed"
    assert result5b == 1, "Test 5b failed"
    assert result5c == 1, "Test 5c failed"
    assert result5d == 1, "Test 5d failed"
    
    print("\nAll test cases passed!")

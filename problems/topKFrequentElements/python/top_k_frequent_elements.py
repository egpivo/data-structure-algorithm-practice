import heapq
from collections import Counter
from typing import List


class Solution:
    """
    Using Counter and sorted.
    Complexity
    ----------
    - TC: O(n log(n))
    - SC: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        sorted_freq = sorted(freq, key=freq.get, reverse=True)
        return sorted_freq[:k]


class SolutionHeap:
    """
    Using heapq.nlargest.
    Complexity
    ----------
    - TC: O(n log(k))
    - SC: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        return heapq.nlargest(k, freq.keys(), key=freq.get)


class SolutionHeap2:
    """
    Using min heap of size k.
    Complexity
    ----------
    - TC: O(n log(k))
    - SC: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = Counter(nums)
        heap = []
        
        for num, count in freq.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)  # Remove element with smallest frequency
        
        # Extract numbers (order doesn't matter per problem statement)
        return [num for _, num in heap]


if __name__ == "__main__":
    solution1 = Solution()
    solution2 = SolutionHeap()
    solution3 = SolutionHeap2()
    
    # Test case 1: Standard case
    nums1 = [1, 1, 1, 2, 2, 3]
    k1 = 2
    result1a = solution1.topKFrequent(nums1, k1)
    result1b = solution2.topKFrequent(nums1, k1)
    result1c = solution3.topKFrequent(nums1, k1)
    print(f"Test 1: {result1a} (Expected: [1, 2] in any order)")
    assert set(result1a) == {1, 2}, "Test 1a failed"
    assert set(result1b) == {1, 2}, "Test 1b failed"
    assert set(result1c) == {1, 2}, "Test 1c failed"
    
    # Test case 2: k equals number of unique elements
    nums2 = [1, 1, 2, 2, 3]
    k2 = 3
    result2a = solution1.topKFrequent(nums2, k2)
    result2b = solution2.topKFrequent(nums2, k2)
    result2c = solution3.topKFrequent(nums2, k2)
    print(f"Test 2: {result2a} (Expected: [1, 2, 3] in any order)")
    assert set(result2a) == {1, 2, 3}, "Test 2a failed"
    assert set(result2b) == {1, 2, 3}, "Test 2b failed"
    assert set(result2c) == {1, 2, 3}, "Test 2c failed"
    
    # Test case 3: k = 1
    nums3 = [1, 1, 1, 2, 2, 3]
    k3 = 1
    result3a = solution1.topKFrequent(nums3, k3)
    result3b = solution2.topKFrequent(nums3, k3)
    result3c = solution3.topKFrequent(nums3, k3)
    print(f"Test 3: {result3a} (Expected: [1])")
    assert result3a == [1], "Test 3a failed"
    assert result3b == [1], "Test 3b failed"
    assert result3c == [1], "Test 3c failed"
    
    # Test case 4: All elements same
    nums4 = [1, 1, 1, 1]
    k4 = 1
    result4a = solution1.topKFrequent(nums4, k4)
    result4b = solution2.topKFrequent(nums4, k4)
    result4c = solution3.topKFrequent(nums4, k4)
    print(f"Test 4: {result4a} (Expected: [1])")
    assert result4a == [1], "Test 4a failed"
    assert result4b == [1], "Test 4b failed"
    assert result4c == [1], "Test 4c failed"
    
    # Test case 5: Single element
    nums5 = [1]
    k5 = 1
    result5a = solution1.topKFrequent(nums5, k5)
    result5b = solution2.topKFrequent(nums5, k5)
    result5c = solution3.topKFrequent(nums5, k5)
    print(f"Test 5: {result5a} (Expected: [1])")
    assert result5a == [1], "Test 5a failed"
    assert result5b == [1], "Test 5b failed"
    assert result5c == [1], "Test 5c failed"
    
    # Test case 6: Negative numbers
    nums6 = [-1, -1, -2, -2, -3]
    k6 = 2
    result6a = solution1.topKFrequent(nums6, k6)
    result6b = solution2.topKFrequent(nums6, k6)
    result6c = solution3.topKFrequent(nums6, k6)
    print(f"Test 6: {result6a} (Expected: [-1, -2] in any order)")
    assert set(result6a) == {-1, -2}, "Test 6a failed"
    assert set(result6b) == {-1, -2}, "Test 6b failed"
    assert set(result6c) == {-1, -2}, "Test 6c failed"
    
    print("\nAll test cases passed!")

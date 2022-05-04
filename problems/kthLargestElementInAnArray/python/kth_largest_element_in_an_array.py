import heapq
import random
from typing import List


class SolutionArray:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Complexity
        ---------
        - TC: O(NlogN) (due to the sort with the worst case)
        - SC: O(1)
        """
        return sorted(nums, reverse=True)[k - 1]


class SolutionHeap:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Complexity
        ---------
        - TC: O(Nlogk) (due to the sort with the worst case)
        - SC: O(1)
        """
        return heapq.nlargest(k, nums)[-1]


class SolutionQuickSelect:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """
        Complexity
        ---------
        - TC: O(N) (worst case: O(N^2))
        - SC: O(1)
        """
        self.nums = nums
        return self.quick_select(0, len(nums) - 1, k)

    def partition(self, left, right, pivot):
        pivot_val = self.nums[pivot]

        self.nums[right], self.nums[pivot] = self.nums[pivot], self.nums[right]

        s = left
        for i in range(left, right):
            if self.nums[i] > pivot_val:
                self.nums[i], self.nums[s] = self.nums[s], self.nums[i]
                s += 1
        self.nums[s], self.nums[right] = self.nums[right], self.nums[s]
        return s

    def quick_select(self, left, right, k):
        pivot = random.randint(left, right)
        mid = self.partition(left, right, pivot)

        if mid == k - 1:
            return self.nums[k - 1]
        elif mid > k - 1:
            return self.quick_select(left, mid - 1, k)
        else:
            return self.quick_select(mid + 1, right, k)


if __name__ == "__main__":
    array = [3, 2, 1, 5, 6, 4]
    k = 2
    print(f"The answer is {SolutionArray().findKthLargest(array, k)}")
    print(f"The answer is {SolutionHeap().findKthLargest(array, k)}")
    print(f"The answer is {SolutionQuickSelect().findKthLargest(array, k)}")

from heapq import heappush, heappop
from typing import List

class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        # Min-heap to store the pairs with the smallest sums
        heap = []
        result = []
        
        # Initialize the heap with pairs (nums1[i], nums2[0]) for the first row
        for i in range(min(k, len(nums1))):  # Only take up to k elements from nums1
            heappush(heap, (nums1[i] + nums2[0], i, 0))  # Push tuple (sum, index in nums1, index in nums2)
        
        # Extract the k smallest pairs
        while heap and len(result) < k:
            sum_val, i, j = heappop(heap)  # Extract the smallest pair
            result.append([nums1[i], nums2[j]])
            
            # If there is a next element in nums2, add the next pair
            if j + 1 < len(nums2):
                heappush(heap, (nums1[i] + nums2[j + 1], i, j + 1))
        
        return result

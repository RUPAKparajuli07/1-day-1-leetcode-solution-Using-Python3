import heapq
from typing import List

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Step 1: Create a min-heap with the first k elements
        heap = nums[:k]
        heapq.heapify(heap)
        
        # Step 2: Iterate through the rest of the elements in nums
        for num in nums[k:]:
            # Step 3: If the current element is larger than the smallest in the heap, replace it
            if num > heap[0]:
                heapq.heapreplace(heap, num)
        
        # Step 4: The root of the heap is the kth largest element
        return heap[0]

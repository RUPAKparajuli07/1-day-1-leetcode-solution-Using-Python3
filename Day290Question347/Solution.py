from collections import Counter
from heapq import heappush, heappop

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # Step 1: Count the frequency of each element
        freq_map = Counter(nums)
        
        # Step 2: Use a min-heap to keep track of top k elements
        heap = []
        for num, freq in freq_map.items():
            heappush(heap, (freq, num))  # Push (frequency, element)
            if len(heap) > k:  # If heap size exceeds k, remove the smallest frequency element
                heappop(heap)
        
        # Step 3: Extract the elements from the heap
        return [num for freq, num in heap]

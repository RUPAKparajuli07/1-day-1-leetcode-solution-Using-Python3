from collections import defaultdict
from typing import List

class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        sum_counts = defaultdict(int)
        
        # Step 1: Compute all sums of pairs from nums1 and nums2
        for a in nums1:
            for b in nums2:
                sum_counts[a + b] += 1
        
        # Step 2: Count valid pairs from nums3 and nums4 that satisfy the sum condition
        count = 0
        for c in nums3:
            for d in nums4:
                count += sum_counts.get(-(c + d), 0)
        
        return count

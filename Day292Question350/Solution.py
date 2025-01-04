from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Create counters for both arrays
        count1 = Counter(nums1)
        count2 = Counter(nums2)
        
        # Find intersection
        intersection = []
        for num in count1:
            if num in count2:
                # Add the number min(count1[num], count2[num]) times
                intersection.extend([num] * min(count1[num], count2[num]))
        
        return intersection

from typing import List

class Solution:
    def totalHammingDistance(self, nums: List[int]) -> int:
        total = 0
        n = len(nums)
        
        # Loop over all 32 bits of integers (0 to 31)
        for i in range(32):
            count_ones = 0
            
            for num in nums:
                # Check if the ith bit is set (1)
                if (num >> i) & 1:
                    count_ones += 1
            
            # count_zeros = total - count_ones
            total += count_ones * (n - count_ones)
        
        return total

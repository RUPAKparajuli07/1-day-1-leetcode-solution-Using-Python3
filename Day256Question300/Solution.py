import bisect

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        sub = []
        
        for num in nums:
            # Find the position to replace in 'sub'
            pos = bisect.bisect_left(sub, num)
            
            if pos == len(sub):
                sub.append(num)  # Extend the sequence
            else:
                sub[pos] = num  # Replace element to keep sub optimal
        
        return len(sub)

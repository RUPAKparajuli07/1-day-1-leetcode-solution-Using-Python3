from typing import List

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        # Step 1: Compute prefix sums
        prefixSum = [0]
        for num in nums:
            prefixSum.append(prefixSum[-1] + num)
        
        # Helper function: Modified merge sort to count range sums
        def merge_sort(start, end):
            # Base case: If the range is empty or single element
            if end - start <= 1:
                return 0
            
            # Divide step: Split the array into two halves
            mid = (start + end) // 2
            count = merge_sort(start, mid) + merge_sort(mid, end)
            
            # Conquer step: Count valid range sums across the two halves
            j = k = mid
            for left in prefixSum[start:mid]:
                # Find the range [lower, upper] for prefixSum differences
                while k < end and prefixSum[k] - left < lower:
                    k += 1
                while j < end and prefixSum[j] - left <= upper:
                    j += 1
                count += (j - k)
            
            # Merge step: Sort the prefix sums to maintain order
            prefixSum[start:end] = sorted(prefixSum[start:end])
            return count
        
        # Step 2: Call the helper function on the full range
        return merge_sort(0, len(prefixSum))

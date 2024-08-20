from typing import List

class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        # Edge case: If there are fewer than 2 elements, return 0
        if len(nums) < 2:
            return 0
        
        # Find the minimum and maximum elements in the array
        min_num, max_num = min(nums), max(nums)
        
        # Calculate the bucket size and number of buckets
        bucket_size = max(1, (max_num - min_num) // (len(nums) - 1))
        bucket_count = (max_num - min_num) // bucket_size + 1
        
        # Initialize the buckets with None (empty state)
        buckets = [[None, None] for _ in range(bucket_count)]
        
        # Place each number in the appropriate bucket
        for num in nums:
            idx = (num - min_num) // bucket_size
            if buckets[idx][0] is None:
                buckets[idx][0] = buckets[idx][1] = num
            else:
                buckets[idx][0] = min(buckets[idx][0], num)
                buckets[idx][1] = max(buckets[idx][1], num)
        
        # Calculate the maximum gap
        max_gap = 0
        previous_max = min_num
        
        for bucket in buckets:
            if bucket[0] is None:
                continue
            max_gap = max(max_gap, bucket[0] - previous_max)
            previous_max = bucket[1]
        
        return max_gap

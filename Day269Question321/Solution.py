from typing import List

class Solution:
    def maxNumber(self, nums1: List[int], nums2: List[int], k: int) -> List[int]:
        def max_subsequence(nums: List[int], length: int) -> List[int]:
            stack = []
            drop = len(nums) - length
            for num in nums:
                while drop and stack and stack[-1] < num:
                    stack.pop()
                    drop -= 1
                stack.append(num)
            return stack[:length]
        
        def merge(subseq1: List[int], subseq2: List[int]) -> List[int]:
            result = []
            while subseq1 or subseq2:
                # Pick the larger lexicographical value from the subsequences
                if subseq1 > subseq2:
                    result.append(subseq1.pop(0))
                else:
                    result.append(subseq2.pop(0))
            return result
        
        max_result = []
        for i in range(max(0, k - len(nums2)), min(k, len(nums1)) + 1):
            subseq1 = max_subsequence(nums1, i)
            subseq2 = max_subsequence(nums2, k - i)
            merged = merge(subseq1[:], subseq2[:])
            max_result = max(max_result, merged)
        
        return max_result

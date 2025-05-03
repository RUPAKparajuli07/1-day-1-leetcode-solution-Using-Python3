from typing import List

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        next_greater = {}

        for num in nums2:
            # Pop smaller elements from the stack and assign their next greater
            while stack and num > stack[-1]:
                prev = stack.pop()
                next_greater[prev] = num
            stack.append(num)

        # Remaining elements in stack have no next greater
        for num in stack:
            next_greater[num] = -1

        # Prepare answer using precomputed next_greater values
        return [next_greater[num] for num in nums1]

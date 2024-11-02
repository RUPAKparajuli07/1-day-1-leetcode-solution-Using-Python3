from collections import deque
from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        # Result array to store max of each sliding window
        result = []
        # Deque to store indices of useful elements in the current window
        deq = deque()

        for i in range(len(nums)):
            # Remove indices of elements not in the current window
            if deq and deq[0] < i - k + 1:
                deq.popleft()

            # Remove elements from the deque that are less than the current element
            while deq and nums[deq[-1]] < nums[i]:
                deq.pop()

            # Add current element's index to deque
            deq.append(i)

            # Start adding maximums to result when the first window of size k is reached
            if i >= k - 1:
                result.append(nums[deq[0]])

        return result

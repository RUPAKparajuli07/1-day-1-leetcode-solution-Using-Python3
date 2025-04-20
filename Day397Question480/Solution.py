from heapq import heappush, heappop
from collections import defaultdict

class Solution:
    def medianSlidingWindow(self, nums, k):
        # Max-heap (as min-heap with negative values)
        small = []
        # Min-heap
        large = []
        # For delayed deletion
        delayed = defaultdict(int)

        # Sizes of the heaps (excluding delayed deletions)
        small_size = 0
        large_size = 0

        def prune(heap):
            while heap:
                num = -heap[0] if heap is small else heap[0]
                if delayed[num]:
                    delayed[num] -= 1
                    heappop(heap)
                else:
                    break

        def balance():
            nonlocal small_size, large_size
            # Ensure size property
            if small_size > large_size + 1:
                val = -heappop(small)
                heappush(large, val)
                small_size -= 1
                large_size += 1
                prune(small)
            elif small_size < large_size:
                val = heappop(large)
                heappush(small, -val)
                small_size += 1
                large_size -= 1
                prune(large)

        def get_median():
            if k % 2 == 1:
                return float(-small[0])
            else:
                return (-small[0] + large[0]) / 2

        res = []

        for i in range(len(nums)):
            num = nums[i]
            # Add num to the correct heap
            if not small or num <= -small[0]:
                heappush(small, -num)
                small_size += 1
            else:
                heappush(large, num)
                large_size += 1

            # Remove element left outside the window
            if i >= k:
                out = nums[i - k]
                delayed[out] += 1
                if out <= -small[0]:
                    small_size -= 1
                    if out == -small[0]:
                        prune(small)
                else:
                    large_size -= 1
                    if out == large[0]:
                        prune(large)

            balance()

            if i >= k - 1:
                res.append(get_median())

        return res

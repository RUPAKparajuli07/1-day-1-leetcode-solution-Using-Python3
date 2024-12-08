import heapq
from typing import List

class Solution:
    def nthSuperUglyNumber(self, n: int, primes: List[int]) -> int:
        # Min-heap to store super ugly numbers
        heap = [1]
        # Set to avoid duplicates
        seen = set(heap)
        # Variable to hold the nth super ugly number
        ugly = 1

        # Generate n super ugly numbers
        for _ in range(n):
            # Get the smallest number from the heap
            ugly = heapq.heappop(heap)
            # Generate new super ugly numbers by multiplying the current number with each prime
            for prime in primes:
                new_ugly = ugly * prime
                # Add to heap only if it hasn't been seen before
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)

        return ugly

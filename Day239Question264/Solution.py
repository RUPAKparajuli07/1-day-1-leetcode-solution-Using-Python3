import heapq

class Solution(object):
    def nthUglyNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Initialize the min-heap with the first ugly number
        heap = [1]
        # Set to keep track of numbers we've already seen to avoid duplicates
        seen = {1}
        
        # Ugly numbers are only generated by multiplying by 2, 3, and 5
        factors = [2, 3, 5]
        
        # We need to pop the smallest ugly number n times
        for _ in range(n - 1):  # The last pop will give us the nth ugly number
            # Pop the smallest number from the heap
            current_ugly = heapq.heappop(heap)
            
            # Generate new numbers by multiplying the current number by each factor
            for factor in factors:
                new_ugly = current_ugly * factor
                if new_ugly not in seen:
                    seen.add(new_ugly)
                    heapq.heappush(heap, new_ugly)
        
        # The top of the heap is the nth ugly number
        return heapq.heappop(heap)
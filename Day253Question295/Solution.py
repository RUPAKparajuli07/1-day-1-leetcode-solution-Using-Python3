import heapq

class MedianFinder:

    def __init__(self):
        # max-heap (stores negative values to simulate max-heap)
        self.max_heap = []
        # min-heap
        self.min_heap = []
    
    def addNum(self, num: int) -> None:
        # Add the number to the max-heap if it's smaller or equal to the root of max-heap
        if len(self.max_heap) == 0 or num <= -self.max_heap[0]:
            heapq.heappush(self.max_heap, -num)
        else:
            heapq.heappush(self.min_heap, num)
        
        # Balance the heaps if their sizes differ by more than 1
        if len(self.max_heap) > len(self.min_heap) + 1:
            # Move the largest element from max-heap to min-heap
            heapq.heappush(self.min_heap, -heapq.heappop(self.max_heap))
        elif len(self.min_heap) > len(self.max_heap):
            # Move the smallest element from min-heap to max-heap
            heapq.heappush(self.max_heap, -heapq.heappop(self.min_heap))

    def findMedian(self) -> float:
        # If the max-heap has more elements, return the root of max-heap
        if len(self.max_heap) > len(self.min_heap):
            return -self.max_heap[0]
        # If both heaps are of equal size, return the average of the roots
        return (-self.max_heap[0] + self.min_heap[0]) / 2.0

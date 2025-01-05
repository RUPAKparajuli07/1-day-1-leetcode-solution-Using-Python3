from sortedcontainers import SortedList

class SummaryRanges:

    def __init__(self):
        # Sorted list to maintain intervals as tuples (start, end)
        self.intervals = SortedList()

    def addNum(self, value: int) -> None:
        # Insert the value as a potential new interval
        new_interval = (value, value)

        # Find if the new value can merge with existing intervals
        idx = self.intervals.bisect_left((value, value))

        # Check and merge with previous interval if necessary
        if idx > 0 and self.intervals[idx - 1][1] + 1 >= value:
            # Merge with the previous interval
            prev_start, prev_end = self.intervals[idx - 1]
            new_interval = (prev_start, max(prev_end, value))
            self.intervals.pop(idx - 1)  # Remove the merged previous interval
            idx -= 1  # Reposition idx to correctly insert new merged interval
        
        # Check and merge with the next interval if necessary
        if idx < len(self.intervals) and self.intervals[idx][0] - 1 <= value:
            # Merge with the next interval
            next_start, next_end = self.intervals[idx]
            new_interval = (new_interval[0], max(new_interval[1], next_end))
            self.intervals.pop(idx)  # Remove the merged next interval
        
        # Insert the merged interval back into the sorted list
        self.intervals.add(new_interval)

    def getIntervals(self) -> list:
        return list(self.intervals)

# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(value)
# param_2 = obj.getIntervals()

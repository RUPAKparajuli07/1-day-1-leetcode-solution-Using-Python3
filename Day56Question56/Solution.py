class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])  # Sort intervals based on the start time
        merged = []
        for interval in intervals:
            # If the merged list is empty or the current interval doesn't overlap with the last merged interval
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # Merge the overlapping intervals
                merged[-1][1] = max(merged[-1][1], interval[1])
        return merged

# Example usage:
intervals1 = [[1,3],[2,6],[8,10],[15,18]]
solution = Solution()
print(solution.merge(intervals1))  # Output: [[1,6],[8,10],[15,18]]

intervals2 = [[1,4],[4,5]]
print(solution.merge(intervals2))  # Output: [[1,5]]

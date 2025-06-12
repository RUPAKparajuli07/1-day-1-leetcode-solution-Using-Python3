from typing import List

class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        # If there are more time points than minutes in a day (1440),
        # there must be a duplicate, so return 0 early.
        if len(timePoints) > 1440:
            return 0

        # Convert each time "HH:MM" to total minutes
        minutes = []
        for time in timePoints:
            h, m = map(int, time.split(":"))
            total_minutes = h * 60 + m
            minutes.append(total_minutes)

        # Sort the minutes
        minutes.sort()

        # Calculate minimum difference between adjacent times
        min_diff = float('inf')
        for i in range(1, len(minutes)):
            diff = minutes[i] - minutes[i - 1]
            min_diff = min(min_diff, diff)

        # Check the circular difference (last and first across midnight)
        circular_diff = 1440 + minutes[0] - minutes[-1]
        min_diff = min(min_diff, circular_diff)

        return min_diff

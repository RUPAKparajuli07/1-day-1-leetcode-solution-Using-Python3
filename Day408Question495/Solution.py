from typing import List

class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        if not timeSeries:
            return 0

        total_poisoned = 0

        for i in range(1, len(timeSeries)):
            gap = timeSeries[i] - timeSeries[i - 1]
            # Add either full duration or the gap (if attack overlaps)
            total_poisoned += min(duration, gap)

        # Add duration for the last attack
        total_poisoned += duration

        return total_poisoned

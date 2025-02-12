from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        
        # Check all possible hours (0-11) and minutes (0-59)
        for hour in range(12):
            for minute in range(60):
                # Count the total number of 1s in binary representations of hour and minute
                if bin(hour).count('1') + bin(minute).count('1') == turnedOn:
                    # Format minute with leading zero if needed
                    result.append(f"{hour}:{minute:02d}")
        
        return result

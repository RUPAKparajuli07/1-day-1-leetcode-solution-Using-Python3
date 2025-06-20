class Solution:
    def checkRecord(self, s: str) -> bool:
        # Check if the student has been absent less than 2 times
        if s.count('A') >= 2:
            return False
        # Check if the student has been late for 3 or more consecutive days
        if "LLL" in s:
            return False
        return True

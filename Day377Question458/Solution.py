import math

class Solution:
    def poorPigs(self, buckets: int, minutesToDie: int, minutesToTest: int) -> int:
        tests = minutesToTest // minutesToDie + 1
        pigs = 0
        
        while (tests ** pigs) < buckets:
            pigs += 1
        
        return pigs

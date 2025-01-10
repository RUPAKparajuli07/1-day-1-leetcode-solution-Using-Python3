from math import gcd

class Solution:
    def canMeasureWater(self, x: int, y: int, target: int) -> bool:
        # If the target exceeds the combined capacity of both jugs, it's not possible
        if target > x + y:
            return False
        
        # Check if the target is a multiple of the gcd of x and y
        return target % gcd(x, y) == 0

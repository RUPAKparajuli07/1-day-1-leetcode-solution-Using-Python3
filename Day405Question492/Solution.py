from typing import List

class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        # Start from the square root of the area
        w = int(area ** 0.5)
        # Decrease w until we find a divisor of area
        while area % w != 0:
            w -= 1
        # Then L can be found as area // w
        return [area // w, w]

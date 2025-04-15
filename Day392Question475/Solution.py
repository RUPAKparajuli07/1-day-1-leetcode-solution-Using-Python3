from bisect import bisect_left

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        radius = 0

        for house in houses:
            # Find the insertion position of house in heaters
            pos = bisect_left(heaters, house)

            # Find distance to the closest heater
            if pos == 0:
                closest_dist = abs(heaters[0] - house)
            elif pos == len(heaters):
                closest_dist = abs(house - heaters[-1])
            else:
                closest_dist = min(abs(house - heaters[pos - 1]), abs(heaters[pos] - house))
            
            radius = max(radius, closest_dist)

        return radius

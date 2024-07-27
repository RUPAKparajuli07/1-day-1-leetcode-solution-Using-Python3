from typing import List


class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_tank, current_tank = 0, 0
        start_station = 0

        for i in range(len(gas)):
            total_tank += gas[i] - cost[i]
            current_tank += gas[i] - cost[i]

            # If current_tank is negative, we can't start from 'start_station' to 'i'
            if current_tank < 0:
                # Start from next station
                start_station = i + 1
                # Reset current_tank
                current_tank = 0

        # If total_tank is negative, it's impossible to complete the circuit
        return start_station if total_tank >= 0 else -1

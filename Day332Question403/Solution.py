from typing import List

class Solution:
    def canCross(self, stones: List[int]) -> bool:
        stone_positions = set(stones)  # Use a set for quick lookup
        dp = {stone: set() for stone in stones}  # DP table with sets
        dp[0].add(0)  # Frog starts at stone 0 with an initial jump of 0
        
        for stone in stones:
            for jump_size in dp[stone]:  # Explore all possible jumps from this stone
                for next_jump in (jump_size - 1, jump_size, jump_size + 1):
                    if next_jump > 0 and (stone + next_jump) in stone_positions:
                        dp[stone + next_jump].add(next_jump)  # Store valid jumps

        return bool(dp[stones[-1]])  # If last stone has valid jumps, return True

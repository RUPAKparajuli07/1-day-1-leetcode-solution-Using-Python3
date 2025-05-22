from functools import lru_cache
from collections import defaultdict

class Solution:
    def findRotateSteps(self, ring: str, key: str) -> int:
        # Step 1: Build a dictionary mapping each character to its indices in ring
        pos = defaultdict(list)
        for i, ch in enumerate(ring):
            pos[ch].append(i)
        
        n = len(ring)
        
        # Step 2: Memoized recursive function
        @lru_cache(None)
        def dfs(index, curr_pos):
            if index == len(key):
                return 0  # Done spelling the key
            
            target_char = key[index]
            min_steps = float('inf')
            
            for target_pos in pos[target_char]:
                # Calculate rotation steps
                rotate_steps = min(abs(curr_pos - target_pos), n - abs(curr_pos - target_pos))
                # 1 extra step for pressing the button
                total_steps = rotate_steps + 1 + dfs(index + 1, target_pos)
                min_steps = min(min_steps, total_steps)
            
            return min_steps
        
        return dfs(0, 0)

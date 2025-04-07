class Solution:
    def canIWin(self, maxChoosableInteger: int, desiredTotal: int) -> bool:
        # If the desired total is 0, the first player has already won
        if desiredTotal <= 0:
            return True
        
        # If the sum of all numbers from 1 to maxChoosableInteger is less than the desired total,
        # it's impossible for the first player to win.
        total_sum = (maxChoosableInteger * (maxChoosableInteger + 1)) // 2
        if total_sum < desiredTotal:
            return False
        
        # Memoization cache: store the result for each state represented by the bitmask
        memo = {}
        
        # Helper function for the recursive DP approach
        def can_win(used: int, total: int) -> bool:
            # If we have already computed the result for this state, return it
            if used in memo:
                return memo[used]
            
            for i in range(maxChoosableInteger):
                # Check if the number i + 1 has already been chosen (by checking if the (i-th) bit is set)
                if (used >> i) & 1:
                    continue
                
                # New state after choosing the number i + 1
                new_total = total + (i + 1)
                
                # If this move results in reaching or exceeding the desired total, the player wins
                if new_total >= desiredTotal:
                    memo[used] = True
                    return True
                
                # Recurse to see if the opponent cannot win in the next state
                # The opponent plays with the remaining numbers (represented by `used | (1 << i)`)
                if not can_win(used | (1 << i), total + (i + 1)):
                    memo[used] = True
                    return True
            
            # If no valid move leads to a win, the player loses from this state
            memo[used] = False
            return False
        
        # Start the game with no numbers used and total score 0
        return can_win(0, 0)

from typing import List

class Solution:
    def countBits(self, n: int) -> List[int]:
        # Initialize the result array with zeros
        ans = [0] * (n + 1)
        
        # Calculate the number of 1's for each number from 1 to n
        for i in range(1, n + 1):
            ans[i] = ans[i // 2] + (i % 2)
        
        return ans

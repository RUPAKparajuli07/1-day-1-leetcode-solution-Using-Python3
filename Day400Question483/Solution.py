import math

class Solution:
    def smallestGoodBase(self, n: str) -> str:
        num = int(n)
        
        # max length of 1s = log2(n), as smallest base is 2
        max_m = int(math.log2(num)) + 1

        for m in range(max_m, 1, -1):  # try lengths from large to small
            left, right = 2, int(num ** (1 / (m - 1))) + 1
            
            while left <= right:
                k = (left + right) // 2
                # use geometric progression formula
                total = (k ** m - 1) // (k - 1)
                
                if total == num:
                    return str(k)
                elif total < num:
                    left = k + 1
                else:
                    right = k - 1
                    
        # If no base found, the only possible base is num - 1 (i.e., 11)
        return str(num - 1)

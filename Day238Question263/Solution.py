class Solution:
    def isUgly(self, n: int) -> bool:
        if n <= 0:
            return False
        
        # Keep dividing n by 2, 3, and 5 as long as it's divisible
        for prime in [2, 3, 5]:
            while n % prime == 0:
                n //= prime
        
        # If n is reduced to 1, it's an ugly number, else it's not
        return n == 1

from typing import List

class Solution:
    def superPow(self, a: int, b: List[int]) -> int:
        MOD = 1337
        
        def mod_pow(x: int, n: int, mod: int) -> int:
            """Efficiently compute (x^n) % mod."""
            result = 1
            x %= mod  # Reduce x within mod
            while n > 0:
                if n % 2 == 1:
                    result = (result * x) % mod
                x = (x * x) % mod
                n //= 2
            return result
        
        # Main computation using the digits of b
        result = 1
        for digit in b:
            # Calculate result for the current digit
            result = mod_pow(result, 10, MOD) * mod_pow(a, digit, MOD) % MOD
        
        return result

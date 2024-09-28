class Solution:
    def countPrimes(self, n: int) -> int:
        # If n is less than 2, there are no prime numbers less than n
        if n < 2:
            return 0
        
        # Create a boolean list to mark prime numbers
        is_prime = [True] * n
        is_prime[0] = is_prime[1] = False  # 0 and 1 are not prime
        
        # Start marking multiples of primes as False (non-prime)
        for i in range(2, int(n**0.5) + 1):
            if is_prime[i]:
                # Mark all multiples of i as non-prime
                for j in range(i * i, n, i):
                    is_prime[j] = False
        
        # Count how many True values remain, which represent primes
        return sum(is_prime)

# Example usage:
solution = Solution()
print(solution.countPrimes(10))  # Output: 4 (primes are 2, 3, 5, 7)

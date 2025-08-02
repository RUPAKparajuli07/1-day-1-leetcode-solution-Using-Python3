class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        num = int(n)
        prefix_len = (length + 1) // 2
        prefix = int(n[:prefix_len])
        
        # Generate palindrome by mirroring prefix
        def create_palindrome(p):
            s = str(p)
            if length % 2 == 0:
                return int(s + s[::-1])
            else:
                return int(s + s[:-1][::-1])

        # Candidate palindromes
        candidates = set()
        for i in [prefix - 1, prefix, prefix + 1]:
            candidates.add(create_palindrome(i))
        
        # Add edge palindromes like 999..9 and 100..001
        candidates.add(10**(length - 1) - 1)
        candidates.add(10**length + 1)
        
        candidates.discard(num)  # Exclude n itself

        # Find closest by absolute difference, then by value
        return str(min(candidates, key=lambda x: (abs(x - num), x)))

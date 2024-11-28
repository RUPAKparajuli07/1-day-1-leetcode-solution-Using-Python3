class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        bulls = 0
        cows = 0
        
        # Dictionaries to count unmatched digits in secret and guess
        secret_count = {}
        guess_count = {}
        
        # First pass: count bulls and prepare counts for unmatched digits
        for i in range(len(secret)):
            if secret[i] == guess[i]:
                bulls += 1
            else:
                secret_count[secret[i]] = secret_count.get(secret[i], 0) + 1
                guess_count[guess[i]] = guess_count.get(guess[i], 0) + 1
        
        # Second pass: count cows from unmatched digits
        for digit in guess_count:
            if digit in secret_count:
                # Cows are the minimum of the counts in secret and guess
                cows += min(secret_count[digit], guess_count[digit])
        
        # Format the result as "xAyB"
        return f"{bulls}A{cows}B"

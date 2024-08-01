from typing import List

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        wordSet = set(wordDict)  # Convert list to set for O(1) lookups
        n = len(s)
        dp = [False] * (n + 1)
        dp[0] = True  # Base case: empty string can always be segmented
        
        for i in range(1, n + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    dp[i] = True
                    break  # No need to check further if dp[i] is True
        
        return dp[n]

from typing import List, Dict

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        wordSet = set(wordDict)
        dp = [[] for _ in range(len(s) + 1)]
        dp[0] = [""]  # Base case: an empty string can be segmented in one way (an empty sentence)

        # Fill the dp table
        for i in range(1, len(s) + 1):
            for j in range(i):
                if dp[j] and s[j:i] in wordSet:
                    for sentence in dp[j]:
                        if sentence:
                            dp[i].append(sentence + " " + s[j:i])
                        else:
                            dp[i].append(s[j:i])
        
        return dp[len(s)]

# Example usage:
sol = Solution()
print(sol.wordBreak("catsanddog", ["cat","cats","and","sand","dog"]))  # Output: ["cats and dog","cat sand dog"]
print(sol.wordBreak("pineapplepenapple", ["apple","pen","applepen","pine","pineapple"]))  # Output: ["pine apple pen apple","pineapple pen apple","pine applepen apple"]
print(sol.wordBreak("catsandog", ["cats","dog","sand","and","cat"]))  # Output: []

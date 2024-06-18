class Solution:
    def numTrees(self, n: int) -> int:
        # Dynamic programming table to store the number of unique BSTs for each count of nodes
        dp = [0] * (n + 1)
        # There is exactly one empty tree
        dp[0] = 1
        
        # Fill the dp array
        for nodes in range(1, n + 1):
            total = 0
            for root in range(1, nodes + 1):
                left = root - 1
                right = nodes - root
                total += dp[left] * dp[right]
            dp[nodes] = total
        
        return dp[n]

# Example usage
sol = Solution()
print(sol.numTrees(3))  # Output: 5
print(sol.numTrees(1))  # Output: 1

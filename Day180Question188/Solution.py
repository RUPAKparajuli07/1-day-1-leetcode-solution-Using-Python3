class Solution:
    def maxProfit(self, k, prices):
        if not prices:
            return 0

        n = len(prices)

        # If k is greater than or equal to n//2, it means we can make unlimited transactions
        if k >= n // 2:
            max_profit = 0
            for i in range(1, n):
                if prices[i] > prices[i - 1]:
                    max_profit += prices[i] - prices[i - 1]
            return max_profit

        # Initialize DP table
        dp = [[0] * n for _ in range(k + 1)]

        for t in range(1, k + 1):
            max_diff = -prices[0]  # Max difference we can get up to day i with one less transaction
            for i in range(1, n):
                dp[t][i] = max(dp[t][i-1], prices[i] + max_diff)
                max_diff = max(max_diff, dp[t-1][i] - prices[i])

        return dp[k][n-1]

# Example usage:
solution = Solution()

k1 = 2
prices1 = [2, 4, 1]
print(solution.maxProfit(k1, prices1))  # Output: 2

k2 = 2
prices2 = [3, 2, 6, 5, 0, 3]
print(solution.maxProfit(k2, prices2))  # Output: 7

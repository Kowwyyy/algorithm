class Solution(object):
    def coinChange(self, coins, amount):
        INF = amount + 1
        dp = [INF] * (amount + 1)
        dp[0] = 0
        for val in range(1, amount + 1):
            for coin in coins:
                if val - coin >= 0:
                    dp[val] = min(dp[val], dp[val - coin] + 1)
        return dp[amount] if dp[amount] != INF else -1

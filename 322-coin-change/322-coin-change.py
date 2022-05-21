class Solution(object):
    def coinChange(self, coins, amount):
        
		dp = [ 10000 for _ in range(amount+1)]

		dp[0] = 0

		for i in range(amount+1):
			for coin in coins:

				if coin <= i:

					dp[i] = min(dp[i],1 + dp[i-coin])

		if dp[-1] == 10000:
			return -1
		else:
			return dp[-1]
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = [float('inf')] * (amount + 1)

        dp[0] = 0
        
        for num in range (1, amount+1):
            for coin in coins:
                if coin <= num:
                    candidate_num = 1 + dp[num - coin]
                    dp[num] = min(dp[num], candidate_num)

        if dp[amount] == float('inf'):
            return -1
            
        return dp[amount]


        
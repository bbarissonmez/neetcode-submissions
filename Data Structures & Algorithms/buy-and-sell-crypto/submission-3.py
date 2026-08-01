class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        max_profit = 0
        known_min = prices[0]

        for i in range (1, len(prices)):
            profit = prices[i] - known_min
            max_profit = max(profit, max_profit)
            known_min = min (prices[i], known_min)

        return max_profit

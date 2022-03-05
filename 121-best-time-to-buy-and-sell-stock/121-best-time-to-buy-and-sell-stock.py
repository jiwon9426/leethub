class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        price, profit = prices[0], 0
        for i in range(1, len(prices)):
            if prices[i] < price:
                price = prices[i]
            profit = max(profit, prices[i]-price)
        return profit
            
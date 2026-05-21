class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        buy=prices[0]
        for i in range(1,len(prices)):
            sell=prices[i]
            profit=sell-buy
            if profit>maxprofit:
                maxprofit=profit
            if prices[i]<buy:
                buy=prices[i]
        return maxprofit



class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        mp=0
        buy=prices[0]
        for i in range(1,len(prices)):
            profit=prices[i]-buy
            if profit>mp:
                mp=profit
            if prices[i]<buy:
                buy=prices[i]
        return mp
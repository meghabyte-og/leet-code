class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        profit=0
        for i in range(1,len(prices)):
            if prices[i]<buy:
                buy=prices[i]

            if prices[i]>buy and prices[i]-buy>profit:
                #print(prices[i],buy)
                profit=prices[i]-buy
            
        return profit
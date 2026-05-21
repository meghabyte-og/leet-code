class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxprofit=0
        minbuy=prices[0]
        for i in range(1,len(prices)):
            curr_sell=prices[i]
            curr_profit=curr_sell-minbuy
            if curr_profit>maxprofit:
                maxprofit=curr_profit
            if curr_sell<minbuy:
                minbuy=curr_sell
        return maxprofit


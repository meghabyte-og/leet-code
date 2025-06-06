class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy=prices[0]
        maxprofit=0

        for i in prices[1:]:
            profit=i-buy
            maxprofit=max(maxprofit,profit)
            buy=min(buy,i)
        return maxprofit
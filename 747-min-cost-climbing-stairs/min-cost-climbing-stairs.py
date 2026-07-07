class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #F(n) = cost(n-1) + min(cost(n-1), cost(n-2))

        cost0 = cost[0]
        cost1 = cost[1]

        for i in range(2, len(cost)):
            cost0, cost1 = cost1, (cost[i] + min(cost0, cost1))
        return min(cost0, cost1)
        
        


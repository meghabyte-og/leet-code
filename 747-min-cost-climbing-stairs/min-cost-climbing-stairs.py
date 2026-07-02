class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        first = cost[0]
        second = cost[1]
        for i in range(2, len(cost)):
            first, second = second, min(first, second) + cost[i]
        return min(first, second)
            

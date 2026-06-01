class Solution:
    def minimumCost(self, cost: List[int]) -> int:
        n = len(cost)
        cost.sort()
        total = 0
        flag = 0
        for i in range(n-1, -1, -1):
            if flag == 2:
                flag = 0
                continue
            flag +=1 
            total += cost[i]
        return total
                
            

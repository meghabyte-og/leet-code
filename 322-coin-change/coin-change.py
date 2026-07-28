class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = [[-1]*(len(coins)+1) for _ in range(amount+1)]

        for i in range(amount+1):
            memo[i][0] = float('inf')
        for j in range(len(coins)+1):
            memo[0][j] = 0

        for i in range(1, amount+1):
            for j in range(1, len(coins)+1):
                if i >= coins[j-1]:
                    memo[i][j] = min(1 + memo[i-coins[j-1]][j-1], 1 + memo[i-coins[j-1]][j], memo[i][j-1])
                else:
                    memo[i][j] = memo[i][j-1]
        return memo[-1][-1] if memo[-1][-1] != float('inf') else -1
                
                

        """
        def dp(amount, i):
            if amount == 0 :
                return 0
                
            if i >= len(coins):
                return float('inf')
            
            if memo[amount][i] != -1:
                return memo[amount][i]
            
            #take the coin
            if amount >= coins[i]:
                memo[amount][i] = min(1 + dp(amount - coins[i], i), 1 + dp(amount - coins[i], i+1), dp(amount, i+1))
            
            #don't take the coin
            else:
                memo[amount][i] = dp(amount, i+1)
            
            return memo[amount][i]
        
        result = dp(amount, 0)
        return result if result != float('inf') else -1
        """
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        
        dp = [[-1]*(len(coins)+1) for _ in range(amount+1)]

        #dp[amount][i]

        for i in range(len(dp[0])):
            dp[0][i] = 1
        
        for i in range(1, len(dp)):
            dp[i][len(coins)] = 0
        
        for i in range(len(coins)-1, -1, -1):
            for a in range(1, amount+1):
                if coins[i] <= a:
                    dp[a][i] = dp[a - coins[i]][i] + dp[a][i+1]
                else:
                    dp[a][i] = dp[a][i+1]
        return(dp[-1][0])

        """
        def dp(amount, i):

            if amount == 0:
                return 1

            if i == len(coins):
                return 0
            
            if memo[amount][i] != -1:
                return memo[amount][i]

            if coins[i] <= amount:
                memo[amount][i] = (dp(amount - coins[i], i) + dp(amount, i+1))

            else:
                memo[amount][i] = dp(amount, i+1)
            
            return memo[amount][i] 

        return(dp(amount, 0))
            
            

        """

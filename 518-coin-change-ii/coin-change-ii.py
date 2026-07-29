class Solution:
    def change(self, amount: int, coins: List[int]) -> int:

        memo = [[-1]*(len(coins)+1) for _ in range(amount+1)]

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
            
            

            

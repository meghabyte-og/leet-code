import math
class Solution:
    def numSquares(self, n: int) -> int:
        
        squares = []
        for i in range(1,n+1):
            if i**2 > n:
                break
            squares.append(i**2)
        
        memo = [[-1]*(len(squares)+1) for _ in range(n+1)]
        
        for i in range(len(memo)):
            memo[i][0] = float('inf')
        
        for j in range(len(memo[0])):
            memo[0][j] = 0
        
        

        for i in range(1, n+1):
            for j in range(1, len(squares)+1):
                if i >= squares[j-1]:
                    memo[i][j] = min(1 + memo[i-squares[j-1]][j], memo[i][j-1])
                else:
                    memo[i][j] = memo[i][j-1]
        return memo[-1][-1]           
                
       


"""
        def dp(squares, n, i):
            if n == 0:
                return 0
            if i >= len(squares):
                return  float('inf')
            
            if memo[n][i] != -1:
                return memo[n][i]

            if n >= squares[i] :
                memo[n][i] =  min(
                    1 + dp(squares, n - squares[i], i), 
                    dp(squares, n, i+1)
                )
            else:
                memo[n][i] = dp(squares, n, i+1)
            return memo[n][i]
        return dp(squares, n, 0)
        """






        
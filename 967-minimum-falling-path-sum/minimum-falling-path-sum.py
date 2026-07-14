class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        memo = {}
        def dp(i,j):
            if i == len(matrix) or j == len(matrix) or i==-1 or j==-1:
                return 0
            if i>= len(matrix):
                return 0
            if j+1>=len(matrix) and j-1<0:
                memo[(i,j)] = matrix[i][j] + dp(i+1,j)
            if j+1>= len(matrix):
                memo[(i,j)] = matrix[i][j] + min(dp(i+1,j-1), dp(i+1, j))
            if j-1<0 :
                memo[(i,j)] = matrix[i][j] + min(dp(i+1,j+1), dp(i+1,j))
            
            if (i,j) in memo:
                return memo[(i,j)]
            memo[(i,j)] = matrix[i][j] + min(dp(i+1,j-1), dp(i+1,j+1), dp(i+1,j))
            return memo[(i,j)]
        
        minimum = float('inf')
        for i in range(len(matrix)):
            memo = {}
            dp(0,i)
            # print(memo)
            minimum = min(minimum, memo[(0,i)])
        return minimum

        
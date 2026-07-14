class Solution:
    def maximalSquare(self, matrix: List[List[str]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        size = min(m, n)
        dp = [[0]*n for _ in range(m)]
        answer = 0

        for j in range(n):
            dp[0][j] = int(matrix[0][j])
            if dp[0][j] == 1:
                answer = 1
        
        for i in range(m):
            dp[i][0] = int(matrix[i][0])
            if dp[i][0] == 1:
                answer = 1
        
    
        for i in range(1,m):
            for j in range(1,n):
                if int(matrix[i][j]) == 0:
                    continue
                dp[i][j] = 1 + min(dp[i-1][j], dp[i-1][j-1], dp[i][j-1])
                answer = max(answer, dp[i][j])
        return answer**2
        

import math
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m=len(obstacleGrid)
        n=len(obstacleGrid[0])
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1] == 1:
            return 0
        reach=[[0]*n for _ in range(m)]
        reach[0][0]=1
        for i in range(1,m):
            if obstacleGrid[i][0]==1:
                break
            reach[i][0]=1
        for j in range(1,n):
            if obstacleGrid[0][j]==1:
                break
            reach[0][j]=1
        
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j]==1:
                    reach[i][j]=0
                    continue
                reach[i][j]=reach[i][j-1]+reach[i-1][j]
        return reach[m-1][n-1]
        
        

            


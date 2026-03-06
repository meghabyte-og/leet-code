class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        min_to_reach=[[500]*len(grid[0]) for i in range(len(grid))]
        m=len(grid)
        n=len(grid[0])
        min_to_reach[0][0]=grid[0][0]
        for i in range(1,m):
            min_to_reach[i][0]=min_to_reach[i-1][0]+grid[i][0]
        for i in range(1,n):
            min_to_reach[0][i]=min_to_reach[0][i-1]+grid[0][i]
        for i in range(1,m):
            for j in range(1,n):
                min_to_reach[i][j]=grid[i][j]+min(min_to_reach[i-1][j],min_to_reach[i][j-1])
        return min_to_reach[m-1][n-1]
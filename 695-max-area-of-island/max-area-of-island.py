class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        visited = [[0]*n for _ in range(m)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def isValid(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            if visited[i][j]:
                return False
            if grid[i][j] == 0:
                return False
            return True
        count = [0]
        def dfs(i,j):
            if not isValid(i,j):
                return 
            visited[i][j] = 1
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if not isValid(ni, nj):
                    continue
                count[0] += 1
                dfs(ni, nj)
            
        maxarea = 0
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == 1:
                    count[0] = 0
                    dfs(i,j)
                    maxarea = max(maxarea, count[0]+1)
        return maxarea
                                

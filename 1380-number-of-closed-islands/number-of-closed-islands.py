class Solution:
    def closedIsland(self, grid: List[List[int]]) -> int:
        # non corner islands
        m = len(grid)
        n = len(grid[0])

        visited = [[0]*n for _ in range(m)]
        directions = [(-1,0), (1,0), (0,-1), (0,1)]

        def isValid(i,j):
            if i<0 or j<0 or i>=m or j>=n:
                return False
            if visited[i][j]:
                return False
            if grid[i][j] == 1:
                return False
            return True 

        def dfs(i,j):
            if not isValid(i,j):
                return 
            
            visited[i][j] = 1
            
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if not isValid(ni, nj):
                    continue
                dfs(ni, nj)
            
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 or i== m-1 or j == n-1:
                    if not visited[i][j] and grid[i][j] == 0 :
                        dfs(i,j)
        
        count = 0        
        for i in range(1, m-1):
            for j in range(1, n-1):
                if not visited[i][j] and grid[i][j] == 0:
                    dfs(i,j)
                    count += 1
        
        return count
            
            


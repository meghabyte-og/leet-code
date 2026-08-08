class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = set()
        m = len(grid)
        n = len(grid[0])
        directions = [(0,1), (0,-1), (1,0), (-1,0)]
        visited = [[0]*n for _ in range(m)]
        count = 0
        def dfs(i,j) -> int:
            if i<0 or j<0 or i>=m or j>=n:
                return 
            if grid[i][j] == '0':
                return 
            if visited[i][j]:
                return 
            visited[i][j] = 1
            for di, dj in directions:
                ni = i + di
                nj = j + dj
                if ni<0 or nj<0 or ni>=m or nj>=n:
                    continue
                if visited[ni][nj]:
                    continue
                if grid[i][j] == '0':
                    continue
                dfs(ni,nj)
            
        for i in range(m):
            for j in range(n):
                if not visited[i][j] and grid[i][j] == '1':
                    dfs(i,j)
                    count +=1 
        return count 
            
                
            
            

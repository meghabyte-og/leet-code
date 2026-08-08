class Solution:
    def shortestBridge(self, grid: List[List[int]]) -> int:
        n = len(grid)
        direction = [[0,1],[0,-1],[1,0],[-1,0]]
        #dfs on an island to make it the "2nd island"
        def dfs(i, j):
            if i < 0 or j < 0 or i >= n or j >= n:
                return  
            if grid[i][j] != 1:
                return 
            grid[i][j] = 2
            for di, dj in direction:
                dfs(i+di, j+dj)
            
        found = 0
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    found = True
                    break
            if found:
                break
        steps = 0
        q = deque()
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    q.append((i,j))
        
        bridge = 0
        while q:
            for _ in range(len(q)):
                curri, currj = q.popleft()
                for di, dj in direction:
                    i = curri + di
                    j = currj + dj

                    if i<0 or j<0 or i>=n or j>=n:
                        continue
                    
                    if grid[i][j] == 2:
                        return steps
                    if grid[i][j] == 0:
                        grid[i][j] = 1
                        q.append((i,j))
            steps+= 1
        
        return steps

                
                



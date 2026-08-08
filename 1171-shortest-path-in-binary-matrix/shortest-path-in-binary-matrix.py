class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        n = len(grid)
        if grid[0][0] == 1 or grid[-1][-1] == 1:
            return -1
        if len(grid)==1:
            if grid[0] == [0]:
                return 1
            else:
                return -1
        visited = [[0]*n for _ in range(n)]
        directions = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        q = deque()
        q.append((0,0))
        visited[0][0] = 1
        step = 1
        while q:
            for _ in range(len(q)):
                curri, currj = q.popleft()
                for di, dj in directions:
                    i = curri + di
                    j = currj + dj
                    
                    #validity
                    if i < 0 or j<0 or i>=n or j>=n:
                        continue
                    if visited[i][j]:
                        continue
                    if grid[i][j] == 1:
                        continue
                    if i == n-1 and j == n-1:
                        return step + 1
                    q.append((i,j))
                    visited[i][j] = 1                   
                    
            step+=1 
        return -1

                
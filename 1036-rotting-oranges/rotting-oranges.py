class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        rows = len(grid)
        cols = len(grid[0])

        fresh = 0
        q = deque()

        for i in range(rows):
            for j in range(cols):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                    continue
                if grid[i][j] == 1:
                    fresh += 1
        
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        minutes = 0

        def isValid(i, j):
            if not 0 <= i < rows:
                return False
            if not 0 <= j < cols:
                return False
            return True

        while q:
            i, j, time = q.popleft()

            minutes = time    
        
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if isValid(ni, nj):
                    if grid[ni][nj] == 1:
                        grid[ni][nj] = 2
                        fresh -= 1
                        q.append((ni,nj,time+1))
        
        return minutes if fresh == 0 else -1


                

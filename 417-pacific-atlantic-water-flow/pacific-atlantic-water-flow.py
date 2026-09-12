class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        m = len(heights)
        n = len(heights[0])

        directions = [(0,1), (1,0), (-1,0), (0,-1)]
        
        def dfs(i, j, visited):
            visited[i][j] = 1
            for di, dj in directions:
                ni, nj = i + di, j + dj
                
                if 0 <= ni < m and 0 <= nj < n and visited[ni][nj] == 0 and heights[ni][nj] >= heights[i][j]:
                    dfs(ni, nj, visited)
        
        pacific = [[0]*n for _ in range(m)]
        atlantic = [[0]*n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0 :
                    if pacific[i][j] == 0:
                        dfs(i, j, pacific)
                if i == m-1 or j == n-1:
                    if atlantic[i][j] == 0:
                        dfs(i, j, atlantic)
                
        result = []
        for i in range(m):
            for j in range(n):
                if pacific[i][j] == 1 and atlantic[i][j] == 1:
                    result.append([i,j])
        
        return result




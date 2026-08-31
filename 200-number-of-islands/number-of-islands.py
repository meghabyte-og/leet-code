class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        def isValid(i,j):
            if i < 0 or j < 0 or i >= len(grid) or j >= len(grid[0]):
                return False
            if grid[i][j] == '0':
                return False
            if visited[i][j] == 1:
                return False
            return True

        directions = [[1,0],[-1,0],[0,1],[0,-1]]
        visited = [[0]*len(grid[0]) for _ in range(len(grid))] 

        def dfs(i, j):
            if not isValid(i,j) :
                return 

            visited[i][j] = 1

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                dfs(ni, nj)
        
        count = 0
        
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if isValid(row, col):
                    count += 1 
                    dfs(row, col)

        return count
            

            
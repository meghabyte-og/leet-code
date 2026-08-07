class Solution:
    def nearestExit(self, maze: List[List[str]], entrance: List[int]) -> int:

        m = len(maze)
        n = len(maze[0])
        visited = [[0]*(n+1) for _ in range(m+1)]

        q = deque()
        q.append(entrance)
        visited[entrance[0]][entrance[1]] = 1
    
        directions = [(0,1), (0,-1), (1,0), (-1,0)]

        count = 0

        while q:
            for _ in range(len(q)):
                ci, cj = q.popleft()
                
                for di, dj in directions:
                    i = ci + di
                    j = cj + dj

                    if i < 0 or j < 0 or i >= m or j >= n:
                        continue
                    if visited[i][j]:
                        continue
                    if maze[i][j] == '+':
                        continue

                    q.append([i,j])
                    visited[i][j] = 1

                    if i == m-1 or j == n-1 or i == 0 or j == 0:
                        return count+1
                
            count += 1
        return -1
            
            



class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        m,n=len(board),len(board[0])
        directions=[[-1,0],[1,0],[0,-1],[0,1]]
        visited=[[False]*n for _ in range (m)]

        def dfs(r,c,i):
            if board[r][c]!=word[i]:
                return False
            if i==len(word)-1:
                return True
            
            visited[r][c]=True
            for rowchange,colchange in directions:
                row,col=r+rowchange,c+colchange
                if 0<=row<m and 0<=col<n and not visited[row][col]:
                    if dfs(row,col,i+1):
                        return True
            visited[r][c]=False
            return False
        for i in range(m):
            for j in range(n):
                if dfs(i, j, 0):
                    return True
        return False
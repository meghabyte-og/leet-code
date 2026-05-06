class Solution:
    def rotateTheBox(self, boxGrid: List[List[str]]) -> List[List[str]]:
        #rotate
        m=len(boxGrid)
        n=len(boxGrid[0])
        newboxGrid = [[0]*m for _ in range(n)]
        for i in range(m):
            for j in range(n):
                newboxGrid[j][m-i-1]=boxGrid[i][j]
        #gravity
        for col in range(m):
            shift = 0
            for i in range(n-1, -1, -1):
                if newboxGrid[i][col] == '*':
                    shift = 0
                elif newboxGrid[i][col] == '.':
                    shift += 1
                elif newboxGrid[i][col] == '#' and shift > 0:
                    newboxGrid[i + shift][col] = '#'
                    newboxGrid[i][col] = '.'
        return newboxGrid          
                        



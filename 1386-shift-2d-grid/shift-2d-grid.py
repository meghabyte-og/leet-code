class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m=len(grid)
        n=len(grid[0])
        arr=[]
        for i in range(m):
            for j in range(n):
                arr.append(grid[i][j])
        arr2=copy.deepcopy(arr)
        for i in range(m*n):
            arr[(i+k)%(m*n)]=arr2[i]
        c=0
        for i in range(m):
            for j in range(n):
                grid[i][j]=arr[(c*n)+j]
            c=c+1
        

        return grid
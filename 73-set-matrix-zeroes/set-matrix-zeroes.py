class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        row=set()
        col=set()
        m=len(matrix)
        n=len(matrix[0])
        for i in range(m):
            for j in range(n):
                if matrix[i][j]==0:
                    row.add(i)
                    col.add(j)
                            
        print(row,col)
        #(1)-  10 11 12 13
        #(0)- 00 10 20 30

        for i in range(m):
            for j in range(n):
                if i in row:
                    matrix[i][j]=0
                if j in col:
                    matrix[i][j]=0
        
        return matrix

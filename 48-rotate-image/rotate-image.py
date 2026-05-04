class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for i in range(n//2):
            #swap row i, n-i-1
            matrix[i],matrix[n-i-1]=matrix[n-i-1],matrix[i]
        
        for i in range(1,n):
            for j in range(i):
                # transpose: swap matrix[i][j], matrix[j][i]
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]
        return matrix
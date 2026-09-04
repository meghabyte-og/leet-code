class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        m = len(matrix)
        n = len(matrix[0])

        result = []

        top = 0 
        bottom = m-1
        left = 0
        right = n-1
        # print(right)

        

        while left <= right and top <= bottom:

            # print('left = ', left,'right=', right,'top = ',top,'bottom=', bottom)

            #left to right
            for i in range(left, right + 1): #0 to n 
                result.append(matrix[top][i])
            
            top += 1
            if len(result) == m*n:
                return result

            for i in range(top, bottom + 1): # 8 12
                result.append(matrix[i][right])
            # print('top -> bottom ', result)
            
            right -= 1
            if len(result) == m*n:
                return result
            
            for i in range(right, left-1, -1): # 12 11 ...
                result.append(matrix[bottom][i])
            # print('right->left', result)
            
            bottom -= 1
            if len(result) == m*n:
                return result
            
            for i in range(bottom, top-1, -1): 
                result.append(matrix[i][left])
            # print('bottom -> top ', result)
            
            left += 1
            if len(result) == m*n:
                return result


        return result

                
        
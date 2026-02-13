class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        n=9
        for i in range(n):
            row=set()
            for j in range(n):
                if board[i][j]!=".":
                    if board[i][j] in row:
                        return False
                    row.add(board[i][j])    
            for j in range(n):
                col=set()
                for i in range(n):
                    if board[i][j]!=".":
                        if board[i][j] in col:
                            return False
                        col.add(board[i][j])
        
        # box
        box=0
        # for i in range(0,9,3): #0 3 6 
        #     for j in range(0,9,3):
        #         seen=()
        #         for k in range(2):
        #             if board[i][j+k] in seen:
        #                 return False
        #             seen.append(board[i][j+k])
        for l in [0,3,6]:
            for k in [0,3,6]:
                seen=set()
                for i in range(0,3):
                    for j in range(0,3):
                        if board[i+l][k+j] in seen:
                            return False
                        else:
                            if board[i+l][j+k]!=".":
                                seen.add(board[i+l][k+j])
            #             print([i+l,j+k],end=" ")
            #         print()
            #     print()
            # print()             
        return True

            
                

            
class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        #[321] [176] [277]
        # [312] [277] [167]
        count=0
        col=[]
        for i in range(len(grid)):
            temp=[]
            for j in range(len(grid)):
                temp.append(grid[j][i])
            col.append(temp)
        # print(grid,col)
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i]==col[j]:
                    count=count+1
        return count

class Solution:
    def findCenter(self, edges: List[List[int]]) -> int:
        adj = set()

        for i,j in edges:
            if i not in adj:
                adj.add(i)
            else:
                return i
            if j not in adj:
                adj.add(j)
            else:
                return j
            
    
        



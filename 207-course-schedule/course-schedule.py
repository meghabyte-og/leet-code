class Solution:
    def canFinish(self, numCourses: int, pre: List[List[int]]) -> bool:
        adj = dict()
        for i in range(numCourses):
            adj[i] = []
        for i,j in pre:
            adj[i].append(j)

        visited = set()
        currpath = set()
        
        def dfs(node):
            visited.add(node)
            currpath.add(node)

            for neighbor in adj[node]:
                if neighbor not in visited:
                    ans = dfs(neighbor)
                    if ans == False:
                        return False
                    currpath.remove(neighbor)
                else:
                    if neighbor in currpath:
                        return False
            return True
        
        for c in range(numCourses):
            if c not in visited:
                ans = dfs(c)
                if ans == False:
                    return False
                if c in currpath:
                    currpath.remove(c)
        return True
            
                    
        

                
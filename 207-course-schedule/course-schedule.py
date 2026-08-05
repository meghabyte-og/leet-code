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
                else:
                    if neighbor in currpath:
                        return False

            currpath.remove(node)
            return True
        
        for c in range(numCourses):
            if c not in visited:
                ans = dfs(c)
                if ans == False:
                    return False
        return True
            
                    
        

                
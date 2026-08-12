class Solution:
    def largestPathValue(self, colors: str, edges: List[List[int]]) -> int:        
        n = len(colors)
        arr = [[0]*26 for _ in range(n)]
        indegree = [0]*n
        adj = dict()
        q = deque()

        for i in range(n):
            adj[i] = []
        
        for i,j in edges:
            adj[i].append(j)
            indegree[j] += 1
        
        for i in range(len(indegree)):
            if indegree[i] == 0:
                q.append(i)
        
        if not q:
            return -1       
        
        processed = 0
        while q:
            curr = q.popleft()
            processed += 1

            arr[curr][ord(colors[curr])-97] += 1
            for neighbor in adj[curr]:
                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    q.append(neighbor)
            
                for i in range(26):
                    arr[neighbor][i] = max(arr[neighbor][i], arr[curr][i])
        if processed != n:
            return -1
        m = 0
        for i in range(len(arr)):
            for j in range(len(arr[0])):
                m = max(m, arr[i][j])
        return m

            



        
        
        
        
        
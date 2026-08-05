class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        adj = dict()
        edge = dict()
        for i in range(n):
            adj[i] = []
            edge[i] = []
        for i,j in connections:
            adj[i].append(j)
            edge[i].append(j)
            edge[j].append(i)
        
        q = deque()
        visited = set()
        visited.add(0)
        q.append(0)

        count = 0
        # bfs = []
        while q:
            curr = q.popleft()
            for neighbor in edge[curr]:
                if neighbor not in visited:
                    visited.add(neighbor)
                    q.append(neighbor)
                    # bfs.append(neighbor)
                    if curr not in adj[neighbor]:
                        count += 1
        # print(bfs)
        return count


            
        
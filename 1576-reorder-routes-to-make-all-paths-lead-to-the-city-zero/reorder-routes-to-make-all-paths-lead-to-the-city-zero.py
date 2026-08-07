class Solution:
    def minReorder(self, n: int, connections: List[List[int]]) -> int:
        undirected = dict()
        directed = dict()
        for i in range(n):
            undirected[i] = []
            directed[i] = []
        for i, j in connections:
            undirected[i].append(j)
            undirected[j].append(i)
            directed[i].append(j)
        
        count = 0
        q = deque()
        q.append(0)
        visited = set()
        visited.add(0)
        while q:
            curr = q.popleft()
            for i in undirected[curr]:
                if i not in visited:
                    visited.add(i)
                    q.append(i)
                    if i in directed[curr]:
                        count += 1
       
        return count

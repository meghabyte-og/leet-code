class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        adj = {i: [] for i in range(n)}
        for i in range(len(manager)):
            if manager[i] !=  -1:
                adj[manager[i]].append(i)
        q = deque()
        q.append((headID, 0))
        time = 0
        while q:
            currnode, currtime = q.popleft()
            for employee in adj[currnode]:
                q.append((employee, currtime + informTime[currnode]))
            time = max(time, currtime)
        return time
                
 
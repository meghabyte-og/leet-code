class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        visited = set()
        def dfs(node):
            visited.add(node)
            for neighbor in rooms[node]:
                if neighbor not in visited:
                    dfs(neighbor)
        
        dfs(0)
        return len(visited) == len(rooms)

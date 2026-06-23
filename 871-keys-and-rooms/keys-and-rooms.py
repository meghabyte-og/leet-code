class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        def dfs(room, visited):
            if room in visited:
                return
            visited.add(room)
            for i in rooms[room]:
                dfs(i, visited)
                if len(visited) == len(rooms):
                    return True
            return False
        return dfs(0, set())

        
            
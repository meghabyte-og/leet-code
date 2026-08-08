class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        visited = set()
        def recurse(i):
            if i < 0 or i>= len(arr):
                return False
            if i in visited:
                return False
            if arr[i] == 0:
                return True
            visited.add(i)
            return recurse(arr[i]+i) or recurse(i-arr[i])
        return recurse(start)
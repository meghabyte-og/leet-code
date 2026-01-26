class Solution:
    def partitionString(self, s: str) -> int:
        seen = {}
        count = 0
        
        for i in s:
            if i in seen:
                count += 1
                seen.clear()
            seen[i]=1
        
        return count + 1


        
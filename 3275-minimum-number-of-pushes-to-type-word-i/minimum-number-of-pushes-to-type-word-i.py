class Solution:
    def minimumPushes(self, word: str) -> int:
        count = 0
        for i in range(len(word)):
            if i<8:
                count += 1
            
            elif i < 16:
                count += 2
            
            elif i< 24:
                count += 3
            
            else:
                count += 4
            
        return count

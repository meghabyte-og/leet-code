class Solution:
    def minFlips(self, s: str) -> int:
        n = len(s)
        s2 = s + s 
        
        flip1 = flip2 = 0  
        ans = float('inf')
        
        for i in range(len(s2)):
            expected1 = '1' if i % 2 else '0'
            expected2 = '0' if i % 2 else '1'  
            
            if s2[i] != expected1:
                flip1 += 1
            if s2[i] != expected2:
                flip2 += 1
            if i >= n:
                left = i - n
                if s2[left] != ('1' if left % 2 else '0'):
                    flip1 -= 1
                if s2[left] != ('0' if left % 2 else '1'):
                    flip2 -= 1
            
            if i >= n - 1:
                ans = min(ans, flip1, flip2)
        
        return ans
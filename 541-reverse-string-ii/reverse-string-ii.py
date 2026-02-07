class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        n=len(s)
        if n<k:
            return s[::-1]
        s=list(s)
        
        for i in range(0,n,2*k):
            s[i:i+k] = reversed(s[i:i+k])  
        return ''.join(s)
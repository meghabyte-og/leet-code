class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i=0
        if len(s)>len(t):
            return False
        if len(s)==0:
            return True
        for j in range(len(t)):
            if s[i]==t[j]:
                i=i+1
                
            if i==len(s):
                return True
        return False

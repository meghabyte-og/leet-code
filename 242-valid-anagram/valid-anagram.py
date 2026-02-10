class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s1={}
        t1={}
        sl=len(s)
        tl=len(t)
        if sl!=tl:
            return False
        for i in range(len(s)):
            if s[i] not in s1:
                s1[s[i]]=1
            else:
                s1[s[i]]+=1
            if t[i] not in t1:
                t1[t[i]]=1
            else:
                t1[t[i]]+=1

        if s1==t1:
            return True
        return False
            
                

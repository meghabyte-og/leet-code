class Solution:
    def removeStars(self, s: str) -> str:
        fin=[]
        for i in range(len(s)):
            if s[i]!="*":
                fin.append(s[i])
            else:
                fin.pop()
        return ''.join(fin)   

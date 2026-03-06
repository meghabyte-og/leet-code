class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        flag=0
        for i in range(len(s)):
            # print(s[i],flag)
            if s[i]=='1' and flag!=-1:
                flag=1
                # print(flag)
                continue
            if s[i]=='0' and flag==1:
                flag=-1
                continue
            
            if s[i]=='1' and flag==-1:
                return False
            
        return True
            

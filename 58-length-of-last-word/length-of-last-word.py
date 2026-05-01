class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s=s.strip()
        n=len(s)
        count=0
        if s=='':
            return 0
        if len(s)==1:
            return 1
        for i in range(n):
            print(s[n-i-1])
            if s[n-i-1]==' ':
                return count
            if n-i-1==0:
                return count+1
            count=count+1



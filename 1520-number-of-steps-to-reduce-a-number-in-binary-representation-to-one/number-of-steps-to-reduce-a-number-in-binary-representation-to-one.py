class Solution:
    def numSteps(self, s: str) -> int:
        n=0
        l=len(s)
        for i in range(l):
            n+=2**i * int(s[l-i-1])
        print(n)
        count=0
        if n==1:
            return 0
        while n>1:
            if n%2==0:
                n=n//2
                count+=1
            else:
                n+=1
                count+=1
            if n==1:
                return count
        

            

class Solution:
    def reverseBits(self, n: int) -> int:
        b=''
        
        while n>0:
            r=int(n%2)
            b=b+str(r)
            n=int(n/2)
        print(b)
        b=b+('0'*(32-len(b) if 32-len(b)>0 else 0))
        b=b[::-1]
        s=0
        for i in range(len(b)):
            s=s+(2**i)*int(b[i])
        return(s)
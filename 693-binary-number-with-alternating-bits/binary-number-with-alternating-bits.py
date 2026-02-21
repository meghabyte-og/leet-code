class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        b=''
        while n>0:
            r=int(n%2)
            n=int(n/2)
            b+=str(r)
            # print(n)
        # print(b)
        for i in range(len(b)-1):
            if b[i+1]==b[i]:
                return False
        return True
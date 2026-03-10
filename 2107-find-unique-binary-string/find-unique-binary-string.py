class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        def tobin(n:int)->str:
            s=''
            if n==0:
                return('0'*len(nums))
            while n>0:
                s+=str(n%2)
                n=int(n/2)
            return s[::-1]
        def todec(s:str)->int:
            n=0
            l=len(s)
            for i in range(l):
                n+=int(s[l-i-1])*(2**i)
            return n
        numbers=[]
        for i in nums:
            numbers.append(todec(i))
        result=''
        for i in range(2**len(nums)):
            if i in numbers:
                continue
            result=tobin(i)
            break
        return '0'*(len(nums)-len(result)) + result
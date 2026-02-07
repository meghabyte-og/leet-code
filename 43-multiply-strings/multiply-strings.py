class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        def getint(nums):
            n=0
            for i in range(len(nums)):
                #n+=(ord(nums[i])-ord('0'))*(10**(max(n-i-1,0))) #399- 3*100 (i=0, n=3)\
                digit=(ord(nums[i])-ord('0'))
                n=(n*10)+digit
            print(n)
            return n
        num1=getint(num1)
        num2=getint(num2)
        return(str(num1*num2))

                
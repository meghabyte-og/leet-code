class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s=0
        n=len(digits)
        for i in range(len(digits)):
            s+=(10**(n-i-1))*digits[i]
        result=[]
        for i in str(s+1):
            result.append(int(i))
        return result
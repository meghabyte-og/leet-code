class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l=[1]
        r=[1]
        n=len(nums)
        final=[]
        leftprod=1
        rightprod=1
        #left
        for i in range(0,n-1):
            leftprod*=nums[i]
            l.append(leftprod)
            rightprod*=nums[n-i-1]
            r.append(rightprod)
        
        for i in range(n):
            final.append(l[i]*r[n-i-1])
        return final        
        
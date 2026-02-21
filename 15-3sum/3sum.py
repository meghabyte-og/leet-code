class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s=[]
        n=len(nums)
        for i in range(n):
            target=nums[i]*(-1)
            if i>0 and nums[i]==nums[i-1]: continue
            seen={}
            for j in range(i+1,n):
                
                c=target-nums[j]
                if c not in seen:
                    seen[nums[j]]=1
                else:
                    s.append(sorted([nums[i],nums[j],0-nums[i]-nums[j]]))
        return list(set(tuple(i) for i in s))
                

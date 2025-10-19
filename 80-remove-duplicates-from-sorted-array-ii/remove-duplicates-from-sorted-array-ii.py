class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen={}
        c=0
        for i in nums:
            if i in seen:
                if seen[i]==1:
                    seen[i]+=1
                    nums[c]=i
                    c=c+1
            else:
                seen[i]=1
                nums[c]=i
                c=c+1
        return c
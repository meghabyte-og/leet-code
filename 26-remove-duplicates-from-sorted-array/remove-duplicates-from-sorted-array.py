class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen={}
        c=0
        for i in nums:
            if i not in seen:
                seen[i]=1
                nums[c]=i
                c=c+1
        return c
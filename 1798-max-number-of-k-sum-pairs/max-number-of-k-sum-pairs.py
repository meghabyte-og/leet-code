class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        i=0
        j=len(nums)-1
        c=0
        nums.sort()
        while i<j:
            if nums[i]+nums[j]==k:
                i+=1
                j-=1
                c+=1
            elif nums[i]+nums[j]>k:
                j=j-1
            else:
                i=i+1
        return c

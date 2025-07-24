class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        i=0
        c=0
        while i<n:
            #print(i,nums,c)
            if nums[i]==0:
                nums.pop(i)
                c=c+1
                n=n-1
                i=i-1
            i=i+1
        nums.extend([0]*c) 
        
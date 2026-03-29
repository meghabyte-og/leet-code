class Solution(object):
    def summaryRanges(self, nums):
        arr=[]
        i=0
        while i<len(nums):
            if nums[i]+1 not in nums:
                arr.append(str(nums[i]))
                i=i+1
            else:
                a=nums[i]
                while nums[i]+1 in nums:
                    i=i+1
                c=""+str(a)+"->"+str(nums[i])
                arr.append(c)
                i=i+1
        return arr
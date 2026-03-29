class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        # if len(nums)==0:
        #     return []
        if len(nums)==1:
            return [str(nums[0])]
        j=0
        result=[]
        for i in range(1,len(nums)):
            # print(nums[j],nums[i-1],nums[i])
            if nums[i-1]!=nums[i]-1:
                # result.append([nums[j],nums[i-1]])
                result.append(str(nums[j])+'->'+str(nums[i-1]) if nums[j]!=nums[i-1] else str(nums[j]))
                j=i
            if i==len(nums)-1 :
                # result.append([nums[j],nums[i]])
                result.append(str(nums[j])+'->'+str(nums[i]) if nums[j]!=nums[i] else str(nums[j]))
        return(result)


                


            
            
            
            


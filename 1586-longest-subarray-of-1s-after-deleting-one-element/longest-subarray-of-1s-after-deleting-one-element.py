class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        maxlen=0
        zeros=0
        right=0
        k=1
        count=0
        for i in range(len(nums)):
            if nums[i]==1:
                count+=1
            else:
                zeros+=1
                #print(zeros,nums[right:i])
                count+=1
                if zeros>k:
                    z=0
                    while z<1:
                        if nums[right]==0:
                            right=right+1
                            count-=1
                            break
                        right=right+1
                        count-=1
                
            maxlen=max(maxlen,count)
            #print(nums[right:i])
        return maxlen-1
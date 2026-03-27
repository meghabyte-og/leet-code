class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if nums[0]>target:
            return 1
        left=0
        if sum(nums)<target:
            return 0
        if sum(nums)==target:
            return len(nums)
        currentsum=0
        windowsize=0
        minwindow=len(nums)+1
        for right in range(len(nums)):
            currentsum+=nums[right]
            windowsize+=1
            # print('right', nums[left:right+1],'window',windowsize, 'sum ', currentsum)
            while currentsum>=target:
                windowsize=min(right-left+1, windowsize)
                currentsum-=nums[left]
                left+=1
                # print('left', nums[left:right+1], 'window',windowsize, 'sum ', currentsum)
                if windowsize<minwindow:
                    minwindow=windowsize
            
        return minwindow
                
                


        

            



            
            
                
    
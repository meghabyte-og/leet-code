class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        if len(nums) == 1:
            return True
        def recurse(start, end):
        
            if start > end:
                return 0

            return max(nums[start] - recurse(start+1, end), nums[end] - recurse(start, end-1))
            
            #  - min(nums[start] + recurse(start+1, end), nums[end] + recurse(start, end-1))
                
            
        
        
        return True if recurse(0, len(nums)-1)>=0 else False

                
            

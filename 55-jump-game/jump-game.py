class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        destintaion=len(nums)-1
        for i in range(len(nums) - 2, -1, -1):
            if nums[i]+i>=destintaion:
                destintaion=i
        if destintaion==0:
            return True
        else:
            return False

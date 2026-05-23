class Solution:
    def check(self, nums: List[int]) -> bool:
        sorted_nums=sorted(nums)
        n=len(nums)
        for i in range(n):
            nums=[nums[n-1]]+nums[:n-1]
            if nums==sorted_nums:
                return True
        return False
            
            
            
class Solution:
    def jump(self, nums: List[int]) -> int:
        count=0
        current_end=0
        farthest=0
        for i in range(len(nums)-1):
            farthest=max(farthest,i+nums[i])
            if i==current_end:
                count+=1
                current_end=farthest
        return count

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        maxs=sum(nums[:k])
        window=maxs
        for i in range(k,len(nums)):
            window+=nums[i]
            window-=nums[i-k]
            if window>maxs:
                maxs=window
        return maxs/k


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n=len(nums)
        res=[]
        for i in range(n):
            for j in range(n):
                if i!=j and nums[i]+nums[j]==target and i not in res and j not in res:
                    res.append(i)
                    res.append(j)
        return res



        
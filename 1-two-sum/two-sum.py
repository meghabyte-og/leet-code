class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen={}
        for i in range(len(nums)):
            c=target-nums[i]
            if c not in seen:
                seen[nums[i]]=i
                continue
            else:
                return [seen[c],i]
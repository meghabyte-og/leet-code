class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        unique=[]
        for i in nums:
            if i not in unique:
                unique.append(i)
        for i in unique:
            if nums.count(i)>len(nums)//2:
                return i
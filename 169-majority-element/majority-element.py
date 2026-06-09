class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        count = 1
        if len(nums) == 1:
            return nums[0]
        
        for i in range(1,len(nums)):
            
            # print(count)
            if nums[i] == nums[i-1]:
                count += 1
                if count > len(nums)//2:
                    return nums[i]

            else:
                count = 1
            

        
            
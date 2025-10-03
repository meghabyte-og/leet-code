class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums1=[]
        for i in range(len(nums)):
            if nums[i]!=val:
                #print(nums[i],end='')
                nums1.append(nums[i])
                #print(nums1,i)
        nums[:]=nums1
        return len(nums1)
                

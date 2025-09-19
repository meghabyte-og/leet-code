class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output=[-1,-1]
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if(nums[mid]==target):
                output[1]=mid
                low=mid+1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        low=0
        high=len(nums)-1
        while low<=high:
            mid=(low+high)//2
            if(nums[mid]==target):
                output[0]=mid
                high=mid-1
            elif nums[mid]>target:
                high=mid-1
            else:
                low=mid+1
        return output

        

        
            


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        n=len(nums)
        if k>n:
            k=k%n
        nums[:]=nums[::-1]
        print(nums)
        nums[:k]=nums[:k][::-1]
        print(nums)
        nums[k:n]=nums[k:n][::-1]    
        print(nums)
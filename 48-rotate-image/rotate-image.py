class Solution:
    def rotate(self, nums: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(nums)
        if n==1:
            return nums
        for i in range(n//2):
            temp=nums[i]
            nums[i]=nums[n-i-1]
            nums[n-i-1]=temp
        
         
        for i in range(1,n):
            for j in range(i):
                #swap nums[i][j] and nums[j][i]
                temp=nums[i][j]
                nums[i][j]=nums[j][i]
                nums[j][i]=temp

        return nums
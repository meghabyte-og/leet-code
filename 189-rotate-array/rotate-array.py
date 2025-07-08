class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        s1=nums[:n-(k%n)]
        s2=nums[n-(k%n):]
        #print(s1,s2)
        nums[:]=s2+s1
        #print(nums)
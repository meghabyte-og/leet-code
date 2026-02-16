class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result=[]
        subset=[]

        def recurse(i):
                
            if i==len(nums):
                result.append(subset[:])
                return
            
            #exclude
            recurse(i+1)
            
            #include
            subset.append(nums[i])
            recurse(i+1)
            subset.pop()

        recurse(0)
        return result

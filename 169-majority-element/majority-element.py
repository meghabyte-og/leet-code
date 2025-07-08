class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        nums.sort()
        n=[]
        l=[]
        for i in nums:
            if i not in n:
                n.append(i)
        for i in n:
            if nums.count(i)>len(nums)/2:
                return i
        
                

            
            

                        


        
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recurse(l):
            if len(l)==0:
                return [[]]
            final=[]
            for i in range(len(l)):
                print(l[:i]+l[i+1:])
                for j in recurse(l[:i]+l[i+1:]):
                    final.append([l[i]]+j)
            print(final)
            return final
        return(recurse(nums))


                       
                
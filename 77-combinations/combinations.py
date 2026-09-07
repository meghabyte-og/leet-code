class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        result = []

        def recurse(sub, start):
            if len(sub) == k:
                result.append(sub[:])
                return

            for i in range(start, n+1):
                sub.append(i)
                recurse(sub, i+1)
                sub.pop()


        recurse([], 1)
        return result



            
            

            
            
            
            
            

                

            
            
            




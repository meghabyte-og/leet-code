class Solution:
    def gcdSum(self, nums: list[int]) -> int:
        def gcd(a: int, b:int) -> int:
            if b == 0:
                return a
            return gcd(b, a%b)

        mx = [nums[0]]
        prefixGcd = [nums[0]]

        for i in range(1, len(nums)):
            mx.append(max(mx[i-1], nums[i]))
            prefixGcd.append(gcd(nums[i], mx[i]))


        prefixGcd = sorted(prefixGcd) 
          

        answer = 0
        for i in range(len(prefixGcd)//2):
            answer += gcd(prefixGcd[i], prefixGcd[len(prefixGcd)-i-1])
        
        return answer
        
        

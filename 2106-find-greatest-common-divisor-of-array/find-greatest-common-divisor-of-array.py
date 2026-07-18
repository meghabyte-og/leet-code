class Solution:
    def findGCD(self, nums: List[int]) -> int:
        def gcd(a:int, b:int) -> int:
            if b == 0:
                return a
            return gcd(b, a%b)
        
        return gcd(min(nums), max(nums))
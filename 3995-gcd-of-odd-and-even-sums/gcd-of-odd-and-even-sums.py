class Solution:
    def gcdOfOddEvenSums(self, n: int) -> int:
        def gcd(a: int, b:int)-> int:
            if b == 0 :
                return a
            return gcd(b, a%b)
        odd = 1
        even = 2
        oddsum = 1
        evensum = 2
        for i in range(n-1):
            odd += 2
            even += 2
            oddsum += odd
            evensum += even
        return gcd(oddsum, evensum)
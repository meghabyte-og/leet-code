class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        low = str(low)
        high = str(high)
        digits = '123456789'
        answer = []
        for i in range(len(low), len(high)+1):
            j = 0 
            while j+i <= len(digits):
                # print(digits[j:j+i])
                curr = int(digits[j: j+i])
                if curr < int(low):
                    j += 1
                    continue
                if curr > int(high):
                    break
                answer.append(curr)
                j += 1
        return answer
class Solution:
    def minimumPushes(self, word: str) -> int:
        frequency = [0] * 26
        for letter in word:
            frequency[ord(letter)-96-1] += 1
        frequency = sorted(frequency, reverse = True)
        return sum(frequency[:8]) + 2*sum(frequency[8: 16]) + 3*sum(frequency[16:24]) + 4*sum(frequency[24:]) 
       
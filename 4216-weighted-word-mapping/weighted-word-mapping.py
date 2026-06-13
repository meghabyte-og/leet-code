class Solution:
    def mapWordWeights(self, words: List[str], weights: List[int]) -> str:
        d = {}
        letters = {}
        result = []
        
        for i in range(len(weights)):
            key = chr(ord('a')+i)
            d[key] = weights[i]
            letter = chr(ord('z')-i)
            letters[i] = letter
        for i in range(len(words)):
            total = 0
            for letter in words[i]:
                total += d[letter]

            result.append(letters[total%26])
        return ''.join(result)
                

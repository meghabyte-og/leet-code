class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        maxbits = max(a.bit_length(), b.bit_length(), c.bit_length())
        a = str(format(a, f'0{maxbits}b'))
        b = str(format(b, f'0{maxbits}b'))
        c = str(format(c, f'0{maxbits}b'))
        count = 0
        for i in range(len(a)):
            print(a[i], 'or', b[i] , ' = ', c[i] )
            if (int(a[i]) or int(b[i]))!= int(c[i]):
                if a[i] == '1' and b[i] == '1':
                    count += 2
                    continue
                count += 1
        return count
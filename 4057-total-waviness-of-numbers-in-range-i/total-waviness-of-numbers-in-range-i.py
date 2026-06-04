class Solution(object):
    def totalWaviness(self, num1, num2):
        count = 0
        for i in range(num1, num2+1):
            i = str(i)
            print(i)
            for j in range(1, len(i)-1):
                
                prev = i[j-1]
                curr = i[j]
                nex = i[j+1]
                if prev < curr > nex or prev > curr < nex:
                    print('True')
                    count += 1
        return count



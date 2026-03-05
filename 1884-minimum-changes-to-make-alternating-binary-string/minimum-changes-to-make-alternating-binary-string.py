class Solution:
    def minOperations(self, s: str) -> int:
        start0 = 0  # mismatches if pattern starts with '0'
        start1 = 0  # mismatches if pattern starts with '1'

        for i, c in enumerate(s):
            expected0 = '0' if i % 2 == 0 else '1'
            expected1 = '1' if i % 2 == 0 else '0'

            if c != expected0:
                start0 += 1
            if c != expected1:
                start1 += 1

        return min(start0, start1)  
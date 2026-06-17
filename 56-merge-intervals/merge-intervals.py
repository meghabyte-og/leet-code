from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        # intervals = sorted(intervals, key = lambda x: x[0])
        intervals.sort(key = lambda x: x[0])
        # print(intervals)
        for interval in intervals:
            if len(result) == 0:
                result.append(interval)
                continue
            if result[-1][0] <= interval[0] <= result[-1][1]:
                result[-1][1] = max(result[-1][1], interval[1])
            elif interval[0] > result[-1][1]:
                result.append(interval)
        return result


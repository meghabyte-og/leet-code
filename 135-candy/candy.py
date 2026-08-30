class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)

        if n == 1:
            return 1

        m = min(ratings)
        arr = [1] * n

        for i in range(1, n):
            if ratings[i] > ratings[i-1]:
                arr[i] = arr[i-1] + 1
            else:
                arr[i] = 1

        for i in range(n-1, 0, -1):
            if ratings[i-1] > ratings[i]:
                arr[i-1] = max(arr[i-1], arr[i] + 1)

        return sum(arr)

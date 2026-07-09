class Solution:
    def pathExistenceQueries(self, n: int, nums: List[int], maxDiff: int, queries: List[List[int]]) -> List[bool]:
        comp = [0] * n
        cid = 0

        for i in range(1, n):
            if abs(nums[i] - nums[i - 1]) > maxDiff:
                cid += 1
            comp[i] = cid
        # print(comp)
        ans = []
        for u, v in queries:
            ans.append(comp[u] == comp[v])

        return ans
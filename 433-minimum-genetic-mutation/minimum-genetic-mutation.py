class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        n = 8
        if startGene == endGene:
            return 0
        if bank == [] and startGene != endGene:
            return -1
        q = deque()
        q.append(startGene)
        visited = set()
        visited.add(startGene)

        bank = set(bank)
        step = 0

        mutations = ['A','G','C', 'T']
        while q:
            for _ in range(len(q)):
                curr = q.popleft()
                if curr == endGene:
                    return step
                for i in range(n):
                    for m in mutations:
                        new = curr[:i] + m + curr[i+1:]
                        if new in bank and new not in visited:
                            q.append(new)
                            visited.add(new)
            step += 1
        return -1

        


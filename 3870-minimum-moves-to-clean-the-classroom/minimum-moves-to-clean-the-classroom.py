from collections import deque
from typing import List

class Solution:
    def minMoves(self, classroom: List[str], energy: int) -> int:
        m = len(classroom)
        n = len(classroom[0])

        litter = {}
        litter_count = 0

        start = None

        for i in range(m):
            for j in range(n):
                if classroom[i][j] == 'S':
                    start = (i, j)
                elif classroom[i][j] == 'L':
                    litter[(i, j)] = litter_count
                    litter_count += 1

        if litter_count == 0:
            return 0

        all_litter = (1 << litter_count) - 1

        q = deque([(start[0], start[1], energy, 0, 0)])

        visited = {}

        directions = [
            (0, 1),
            (0, -1),
            (1, 0),
            (-1, 0)
        ]

        while q:
            i, j, current_energy, mask, moves = q.popleft()

            if mask == all_litter:
                return moves

            state = (i, j, mask)
            if state in visited and visited[state] >= current_energy:
                continue

            visited[state] = current_energy

            if current_energy == 0:
                continue

            for di, dj in directions:
                ni = i + di
                nj = j + dj

                if ni < 0 or nj < 0 or ni >= m or nj >= n:
                    continue

                if classroom[ni][nj] == 'X':
                    continue

                new_energy = current_energy - 1
                new_mask = mask

                if classroom[ni][nj] == 'R':
                    new_energy = energy

                elif classroom[ni][nj] == 'L':
                    new_mask |= 1 << litter[(ni, nj)]

                state = (ni, nj, new_mask)

                # Don't enqueue if we've already reached this state
                # with at least as much energy.
                if state in visited and visited[state] >= new_energy:
                    continue

                q.append((
                    ni,
                    nj,
                    new_energy,
                    new_mask,
                    moves + 1
                ))

        return -1

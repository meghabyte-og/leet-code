from functools import lru_cache

class Solution:
    def totalWaviness(self, num1: int, num2: int) -> int:
        def prefix(n: int) -> int:
            if n < 0:
                return 0

            s = str(n)
            m = len(s)

            @lru_cache(None)
            def dp(pos, tight, started, length_state, last2, last1):
                if pos == m:
                    return (1, 0)

                limit = int(s[pos]) if tight else 9

                total_cnt = 0
                total_wavy = 0

                for d in range(limit + 1):
                    ntight = tight and (d == limit)

                    if not started:
                        if d == 0:
                            cnt, wav = dp(
                                pos + 1, ntight, 0, 0, 0, 0
                            )
                        else:
                            cnt, wav = dp(
                                pos + 1, ntight, 1, 1, 0, d
                            )

                    else:
                        if length_state == 1:
                            cnt, wav = dp(
                                pos + 1, ntight, 1, 2, last1, d
                            )
                        else:
                            inc = int(
                                (last1 > last2 and last1 > d) or
                                (last1 < last2 and last1 < d)
                            )

                            cnt, wav = dp(
                                pos + 1, ntight, 1, 2, last1, d
                            )

                            wav += inc * cnt

                    total_cnt += cnt
                    total_wavy += wav

                return total_cnt, total_wavy

            return dp(0, 1, 0, 0, 0, 0)[1]

        return prefix(num2) - prefix(num1 - 1)
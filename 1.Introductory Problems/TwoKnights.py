import math


def solve(n):
    for i in range(1, n + 1):
        total = math.comb(i * i, 2)
        # 2 * 3 count == 3 * 2 count
        cnt = (i - 2) * (i - 1)
        total -= 4 * cnt
        print(total)


n = int(input())
solve(n)

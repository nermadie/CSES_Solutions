def solve(n, p, i, result):
    if i == 0:
        return result
    return min(
        solve(n, p, i - 1, abs(result + p[n - i])),
        solve(n, p, i - 1, abs(result - p[n - i])),
    )


n = int(input())
p = list(map(int, input().split()))
print(solve(n, p, n, 0))

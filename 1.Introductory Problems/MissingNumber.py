def solve(n, a):
    total = sum(a)
    return ((n + 1) * n) // 2 - total


n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

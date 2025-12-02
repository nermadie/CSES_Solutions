def solve(a, b):
    if a == b:
        if a % 3 == 0 and b % 3 == 0:
            return "YES"
        else:
            return "NO"

    large = max(a, b)
    small = min(a, b)
    diff = large - small
    large -= diff * 2
    small -= diff
    if large == small and large >= 0 and large % 3 == 0:
        return "YES"
    else:
        return "NO"


t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    print(solve(a, b))

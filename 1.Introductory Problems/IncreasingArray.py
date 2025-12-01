def solve(n, a):
    result = 0
    cur_max = a[0]
    for i in range(n - 1):
        cur_max = max(cur_max, a[i])
        if a[i + 1] < cur_max:
            result += cur_max - a[i + 1]
    return result


n = int(input())
a = list(map(int, input().split()))
print(solve(n, a))

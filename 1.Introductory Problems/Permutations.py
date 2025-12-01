def solve(n):
    if n == 1:
        print(1)
        return
    result = []
    for i in range(2, n + 1, 2):
        result.append(i)
    if abs(result[-1] - 1) <= 1:
        print("NO SOLUTION")
        return
    for i in range(1, n + 1, 2):
        result.append(i)
    print(" ".join(map(str, result)))


n = int(input())
solve(n)

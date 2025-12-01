"""
Max point: n - 1
Min point: 0
Max sum: n
"""


def solve(n, a, b):
    if (a > n - 1 or b > n - 1) or (a + b > n):
        print("NO")
        return
    if (a == 0 and b != 0) or (b == 0 and a != 0):
        print("NO")
        return
    print("YES")
    diff = n - a - b
    a_points = []
    b_points = []

    for i in range(diff):
        a_points.append(i + 1)
        b_points.append(i + 1)
    for i in range(a):
        a_points.append(n - i)
        b_points.append(a - i + diff)
    for i in range(b):
        b_points.append(n - i)
        a_points.append(b - i + diff)
    print(" ".join(map(str, a_points)))
    print(" ".join(map(str, b_points)))


t = int(input())
for _ in range(t):
    n, a, b = map(int, input().split())
    solve(n, a, b)

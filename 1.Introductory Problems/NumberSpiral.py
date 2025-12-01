"""
1 + 2 + 4 + 6 + 8
(((n - 1) * 2 + 2) * (n - 1)) // 2
"""


def solve(t, y, x):
    max_dim = max(y, x)
    is_top_increase = max_dim % 2 != 0
    cur_diag = (((max_dim - 1) * 2 + 2) * (max_dim - 1)) // 2

    if x < max_dim:
        if is_top_increase:
            return cur_diag - (max_dim - x) + 1
        else:
            return cur_diag + (max_dim - x) + 1
    else:
        if is_top_increase:
            return cur_diag + (max_dim - y) + 1
        else:
            return cur_diag - (max_dim - y) + 1


t = int(input())
for _ in range(t):
    y, x = map(int, input().split())
    print(solve(t, y, x))

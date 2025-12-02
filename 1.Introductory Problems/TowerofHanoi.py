"""
T1: last
T2: top
T3: nothing
"""


def move(order_list, n):
    if n == 1:
        print(order_list[0], order_list[2])
        return
    move([order_list[0], order_list[2], order_list[1]], n - 1)
    print(order_list[0], order_list[2])
    move([order_list[1], order_list[0], order_list[2]], n - 1)


def solve(n):
    result = 0
    for i in range(n):
        result = result * 2 + 1
    print(result)
    order_list = [1, 2, 3]
    move(order_list, n)


n = int(input())
solve(n)

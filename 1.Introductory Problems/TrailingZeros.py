"""
2
4
6
8
10

5: less than 2 -> count 5 to cal
Be careful about multiples of 25, 125, ...
"""


def solve(n):
    result = 0
    power_of_5 = 1
    while 5**power_of_5 <= n:
        result += n // (5**power_of_5)
        power_of_5 += 1
    return result


n = int(input())
print(solve(n))

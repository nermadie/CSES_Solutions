"""
00000 -> 01111
01111 -> 11111
11111 -> 10000
"""


def convert(s, index):
    if s[index] == "0":
        s[index] = "1"
    else:
        s[index] = "0"
    return s


def solve(n):
    cur_result_list = [""]
    for i in range(n):
        temp_list = []
        for item in cur_result_list:
            temp_list.append("0" + item)
        for item in reversed(cur_result_list):
            temp_list.append("1" + item)
        cur_result_list = temp_list

    for item in cur_result_list:
        print(item)


n = int(input())
solve(n)

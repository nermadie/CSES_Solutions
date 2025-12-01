def solve(s):
    max_cnt = 0
    cnt = 1
    for i in range(len(s) - 1):
        if s[i + 1] == s[i]:
            cnt += 1
        else:
            max_cnt = max(max_cnt, cnt)
            cnt = 1
    max_cnt = max(max_cnt, cnt)
    return max_cnt


s = input().strip()
print(solve(s))

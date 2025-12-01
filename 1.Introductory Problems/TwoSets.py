def solve(n):
    if n == 1:
        print("NO")
        return
    total = ((n + 1) * n) // 2
    if total % 2 != 0:
        print("NO")
        return
    first_list = []
    second_list = []
    cur_count = 0
    for i in range(n, 0, -1):
        if cur_count + i > total // 2:
            second_list.append(i)
            continue
        first_list.append(i)
        cur_count += i

    print("YES")
    print(len(first_list))
    print(" ".join(map(str, first_list)))
    print(len(second_list))
    print(" ".join(map(str, second_list)))


n = int(input())
solve(n)

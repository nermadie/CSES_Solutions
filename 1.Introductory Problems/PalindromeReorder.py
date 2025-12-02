def solve(s):
    library = {}
    for char in s:
        if char in library:
            library[char] += 1
        else:
            library[char] = 1
    odd_count = 0
    result = ""
    for char in library:
        if library[char] % 2 != 0:
            odd_count += 1
            result = char * library[char]
    if odd_count > 1:
        return "NO SOLUTION"

    for char in library:
        if library[char] % 2 == 0:
            result = char * (library[char] // 2) + result + char * (library[char] // 2)
    return result


s = input().strip()
print(solve(s))

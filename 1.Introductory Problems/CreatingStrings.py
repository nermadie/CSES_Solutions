from math import factorial, prod


def create_string_permutations(dict_items, cur_string):
    empty_check = True
    for key, value in dict_items:
        if value != 0:
            empty_check = False
            break
    if empty_check:
        print(cur_string)
    dict_words = dict(dict_items)
    for key, value in dict_words.items():
        if value > 0:
            dict_words[key] -= 1
            create_string_permutations(dict_words.items(), cur_string + key)
            dict_words[key] += 1


def solve(s):
    dict_words = {}
    for char in s:
        if char in dict_words:
            dict_words[char] += 1
        else:
            dict_words[char] = 1
    print(factorial(len(s)) // prod(factorial(v) for v in dict_words.values()))

    dict_words = dict(sorted(dict_words.items()))

    if len(s) > 1:
        for key, value in dict_words.items():
            if value > 0:
                dict_words[key] -= 1
                create_string_permutations(dict_words.items(), key)
                dict_words[key] += 1
    else:
        print(s)


s = input().strip()
solve(s)

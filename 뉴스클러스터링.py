# https://programmers.co.kr/learn/courses/30/lessons/17677


def split_list(str):
    split_list = []
    str = str.lower()
    for i in range(len(str)-1):
        temp = str[i]
        if 'a' <= temp <= 'z' and 'a' <= str[i+1] <= 'z':
            temp += str[i+1]
            split_list.append(temp)
        else:
            continue

    return split_list


def solution(str1, str2):
    set_str1 = split_list(str1)
    set_str2 = split_list(str2)

    if len(set_str1) == 0 and len(set_str2) == 0:
        return 65536

    intersection = [x for x in set_str1 if x in set_str2]

    temp = set_str2.copy()
    union = set_str2 + [x for x in set_str1 if not x in set_str2 or temp.remove(x)]

    answer = len(intersection) / len(union)

    return int(answer * 65536)
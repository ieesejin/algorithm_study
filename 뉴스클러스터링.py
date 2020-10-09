# https://programmers.co.kr/learn/courses/30/lessons/17677


# str이 들어오면 특수문자를 제외하고 두글자씩 끊어서 리턴
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


# def another_split(str):
#     str = str.lower()
#
#     return [str[i:i+2] for i in range(len(str)-1) if str[i:i+2].isalpha()]


def solution(str1, str2):
    set_str1 = split_list(str1)
    set_str2 = split_list(str2)

    # 둘다 공집합이면 1을 리턴 * 65536
    if len(set_str1) == 0 and len(set_str2) == 0:
        return 65536

    # 합, 교 갯수만 구하면됨
    union = 0
    intersect = 0
    for str in set(set_str1 + set_str2):
        union += max(set_str1.count(str), set_str2.count(str)) # 중복이 가능하므로 둘중 갯수중 많은것으로 갯수를 포함하면됨
        intersect += min(set_str1.count(str), set_str2.count(str)) # 교집합은 갯수가 작은것으로

    answer = intersect / union

    return int(answer * 65536)

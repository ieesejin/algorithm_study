# https://programmers.co.kr/learn/courses/30/lessons/72410


def solution(new_id):
    answer = ''

    # 1단계
    new_id = new_id.lower()

    # 2단계
    for i in new_id:
        # if c.isalpha() or c.isdigit() or c in ['-', '_', '.']:
        if 'a' <= i <= 'z' or '0' <= i <= '9' or i == '-' or i == '_' or i == '.':
            answer += i

    # 3단계
    # while '..' in answer:
    #     answer = answer.replace('..', '.')
    for i in range(len(answer), 1, -1):
        answer = answer.replace('.' * i, '.')

    # 4단계
    if answer == '.':
        answer = ''
    elif answer[0] == '.':
        answer = answer[1:]
    elif answer[-1] == '.':
        answer = answer[:-1]

    # 5단계
    if answer == '':
        answer = 'a'

    # 6단계
    if len(answer) >= 16:
        answer = answer[:15]
        if answer[-1] == '.':
            answer = answer[:-1]

    # 7단계
    if len(answer) <= 2:
        while len(answer) < 3:
            answer += answer[-1]

    return answer



print(solution("...!@BaT#*..y.abcdefghijklm"))	# "bat.y.abcdefghi"
print(solution("z-+.^.")) # "z--"
print(solution("=.=")) # "aaa"
print(solution("123_.def")) # "123_.def"
print(solution("abcdefghijklmn.p")) # "abcdefghijklmn"
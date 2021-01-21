# https://programmers.co.kr/learn/courses/30/lessons/60058


def solution(p):
    def split(p):
        str1 = ''
        str2 = ''
        count1 = 0
        count2 = 0

        for i in range(len(p)):
            str1 += p[i]
            if p[i] == '(':
                count1 += 1
            if p[i] == ')':
                count2 += 1

            if count1 == count2:
                str2 = p[i + 1:]
                break

        return str1, str2

    def right(p):
        result = False
        count1 = 0
        count2 = 0

        for i in range(len(p)):
            if p[i] == '(':
                count1 += 1
            if p[i] == ')':
                count2 += 1

            if count2 > count1:
                return result

        if count1 == count2:
            result = True

        return result

    if len(p) == 0:
        return ''

    u, v = split(p)

    if right(u):
        return u + solution(v)
    else:
        answer = '('
        answer += solution(v)
        answer += ')'

        new_u = u[1:-1]
        for i in range(len(new_u)):
            if new_u[i] == '(':
                answer += ')'
            if new_u[i] == ')':
                answer += '('

        return answer


print(solution("(()())()")) # expected result: "(()())()"

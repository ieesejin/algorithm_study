# https://programmers.co.kr/learn/courses/30/lessons/42883#


def solution1(number, k):
    stack = []

    for i in range(len(number)):
        if len(stack) == 0:
            stack.append(number[i])
            continue

        finish = False # for break the loop

        while stack and int(number[i]) > int(stack[-1]): # check stack, if number[i] is bigger pop the stack until stack[-1] is bigger
            stack.pop()
            k -= 1
            if k == 0:
                stack += number[i:]
                finish = True
                break

        if finish: # if k == 0
            break

        stack.append(number[i])

    # if k is not 0, slick k back side of stack
    return ''.join(stack)[:len(number) - k] if k != 0 else ''.join(stack)


print(solution1("4177252841", 4)) # expected result = "775841"


def solution2(number, k):
    stack = [number[0]]
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0:
            k -= 1
            stack.pop()
        stack.append(num)
    if k != 0:
        stack = stack[:-k]
    return ''.join(stack)


print(solution2("4177252841", 4)) # expected result = "775841"

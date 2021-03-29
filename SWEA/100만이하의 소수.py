# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV_6mRsasV8DFAWS&categoryId=AV_6mRsasV8DFAWS&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=6
answers = []

for i in range(2, 1000000):
    if i == 2:
        answers.append(2)
        continue

    for j in range(2, int(i ** 0.5)+1):
        if i % j == 0:
            break
    else:
        answers.append(i)

for i in range(len(answers)):
    print("{} ".format(answers[i]), end="")


# 에라토스
# def eratos(n):
#     num = [True for _ in range(n + 1)]
#     num[0] = False
#     num[1] = False
#
#     for i in range(2, n + 1):
#         if num[i]:
#             for j in range(i + i, n + 1, i):
#                 num[j] = False
#     return num
#
#
# answer = eratos(1000000)
# for i in range(len(answer)):
#     if answer[i]:
#         print(i, end=" ")
# https://swexpertacademy.com/main/code/problem/problemDetail.do?problemLevel=3&contestProbId=AV-Tj7ya3jYDFAXr&categoryId=AV-Tj7ya3jYDFAXr&categoryType=CODE&problemTitle=&orderBy=FIRST_REG_DATETIME&selectCodeLang=PYTHON&select-1=3&pageSize=10&pageIndex=7


import heapq

T = int(input())
answer = []

for test_case in range(T):
    case_answer = []
    heap = []
    N = int(input())
    for i in range(N):
        operation = list(map(int, input().split()))
        if len(operation) == 2:
            heapq.heappush(heap, (-operation[-1], operation[-1]))

        if len(operation) == 1:
            if len(heap) == 0:
                case_answer.append(-1)
            else:
                case_answer.append(heapq.heappop(heap)[1])

    answer.append(case_answer)

print(answer)
for i in range(len(answer)):
    res = "#{} ".format(i+1) + ' '.join(map(str, answer[i]))
    print(res)
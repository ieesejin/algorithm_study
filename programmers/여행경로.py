# https://programmers.co.kr/learn/courses/30/lessons/43164


def solution(tickets):
    answer = []

    routes = dict()  # 티켓을 key: 출발지 value: 갈수 있는 곳 으로 정리
    for ticket in tickets:  # 티켓들을 딕셔너리로 정리
        if ticket[0] not in routes:
            routes[ticket[0]] = [ticket[1]]
        else:
            routes[ticket[0]].append(ticket[1])

    for key in routes.keys():  # 티켓의 value 들을 내림 차순으로 정리 --> 내림 차순으로 해야지 뽑았을 때 오름 차순이 됨
        routes[key].sort(reverse=True)

    stack = ["ICN"]  # 출발은 항상 ICN
    while stack:
        start = stack[-1]
        if start not in routes or len(routes[start]) == 0:  # start가 더 이상 출발 지역이 아닐 때, 출발 지역이었지만 더이상 갈 수 있는 곳이 없을 때
            answer.append(stack.pop())
        else:
            stack.append(routes[start].pop())  # start에서 갈 수 있는 곳을 스택에 넣어줌

    return answer[::-1]


print(solution([["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]))  # expected result: ["ICN", "JFK", "HND", "IAD"]

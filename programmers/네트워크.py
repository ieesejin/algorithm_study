# https://programmers.co.kr/learn/courses/30/lessons/43162


def dfs(computers, visited, s): # 연결되있는 컴퓨터들을 1로 바꿔줌
    stack = [s]
    while stack:
        tmp = stack.pop()
        if visited[tmp] == 0:
            visited[tmp] = 1
        for i in range(len(computers)):
            if computers[tmp][i] == 1 and visited[i] == 0:
                stack.append(i)


def solution(n, computers):
    answer = 0
    visited = [0 for _ in range(n)] # 네크워크에 속한 컴퓨터를 1로 바꿔 체크하기 위한 리스트

    i = 0
    while 0 in visited: # 모든 컴퓨터가 네트워크에 속할 때 까지
        if visited[i] == 0:
            dfs(computers, visited, i)
            answer += 1
        i += 1

    return answer
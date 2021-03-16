# https://programmers.co.kr/learn/courses/30/lessons/43163


from collections import deque  # bfs 사용


def solution(begin, target, words):
    answer = 0
    if target not in words:  # 타겟이 없으면 바로 리턴 가능
        return 0

    visited = {begin}  # 이미 바꿔본 문자를 담아 집합으로 정의
    q = deque([(begin, 0)])  # 시작 (단어, 바꾼 횟수)

    while q:
        w, cnt = q.popleft()
        if w == target:  # 탈출 조건
            return cnt  # 문제 요구사항 몇번 바꿔서 탈출 하는지

        for word in words:  # 한글자만 차이 나는 단어를 큐에 추가
            diff_cnt = 0
            for i in range(len(w)):
                if w[i] != word[i]:  # 차이 나는 글자 갯수 체크
                    diff_cnt += 1
            if diff_cnt == 1:  # 한자 차이날 때 큐에 추가하고 방문한 단어에 추가
                q.append((word, cnt + 1))
                visited.add(word)

    return answer


print(solution("hit", "cog", ["hot", "dot", "dog", "lot", "log", "cog"]))  # expected result: 4
